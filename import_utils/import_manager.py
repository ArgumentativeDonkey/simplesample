from pathlib import Path

from PySide6.QtCore import QObject, Signal

SUPPORTED_AUDIO_FILES = ['.mp3', '.wav', '.ogg', '.m4a', '.aac', '.ogv', '.mp4', '.flac', '.mkv', '.avi', '.mov', '.m4v', '.mjpeg']

class ImportManager(QObject):
    imported_paths: list[Path] = []
    storage_path: Path | None = None
    new_paths: Signal = Signal(list)

    def __init__(self, storage_path: Path | None = None):
        super().__init__()
        if storage_path is not None:
            self.storage_path = storage_path
        if self.storage_path is not None:
            try:
                with self.storage_path.open("r", encoding="utf-8") as f:
                    print("retrieving imported paths...")
                    lines = f.readlines()
                    self.imported_paths = [Path(line.strip()) for line in lines]
                    print("imported paths imported!")
            except FileNotFoundError:
                print("storage_path not found.")

    def tidy(self):
        """Tidies up imports by removing an import if it does not exist or is no longer a file"""
        self.imported_paths = [path for path in self.imported_paths if path.exists() and path.is_file()]

    def import_file(self, path: Path):
        """Import a single file into the manager.

        Args:
            path (Path): The path to the file. Must point to an audio file (.mp3, .wav, .ogv, .mp4, .flac).
        """
        if not path.exists():
            raise FileNotFoundError("that location does not exist")

        if not path.is_file():
            raise FileNotFoundError("that location isn't a file")

        if path.suffix not in SUPPORTED_AUDIO_FILES:
            raise ValueError("that isn't an audio file")
            
        if path in self.imported_paths:
            raise ValueError("that's already been imported")

        self.imported_paths.append(path)
        self.new_paths.emit([path])
        print(f"{path.name} imported")

    def import_directory(self, path: Path) -> int:
        """Import the entire contents of a directory (including is subdirectories).
        All files, regardless of type, will try to be imported.
        This will not throw an exception if the directory is empty or contains no audio files.

        Args:
            path (Path): The path to the directory. Must point to a directory.

        Returns:
            The number of files added to the import manager
        """
        if not path.exists():
            raise FileNotFoundError("that location does not exist")

        if not path.is_dir():
            raise ValueError("that location leads to a directory, not a file")

        print(f"importing {path}...")
        imported: list[Path] = []
        files = [path for path in path.rglob("*") if path.is_file()]
        for file in files:
            try:
                self.import_file(file)
                imported.append(file)
            except ValueError:
                pass
            except FileNotFoundError as e:
                print(f"internal error detected when trying to import {file}: {e}")
        print(f"{imported} files from {path} imported")
        return len(imported)

    def import_path(self, path: Path) -> int:
        """Import from a Path. Automatically detects whether a path is a file or a directory.

        Args:
            path (Path): The path to whatever you are trying to import.
        """
        if path.is_file():
            self.import_file(path)
            return 1
        else:
            return self.import_directory(path)
    
    def save(self, storage_path: Path | None = None):
        if storage_path is not None:
            self.storage_path = storage_path

        if self.storage_path is None:
            raise AttributeError("no storage path was provided nor stored")

        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

        with self.storage_path.open("w", encoding="utf-8") as f:
            print("storing imported paths")
            strings = [str(path) + '\n' for path in self.imported_paths]
            f.writelines(strings)
            print("imported paths stored!")

    def remove(self, path: Path):
        self.imported_paths.remove(path)

if __name__ == "__main__":
    pass