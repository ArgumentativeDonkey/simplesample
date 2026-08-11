from pathlib import Path

class ImportManager:
    imported_files: list[Path] = []
    index_path = None

    def __init__(self, index_path: Path | None = None):
        if index_path is not None:
            self.index_path = index_path
        with open(index_file, "r") as f:
            
            pass

    def import_file(self, path: Path):
        if not path.exists():
            raise ValueError("path does not exist")
        if not path.is_file():
            raise ValueError("path does not point to a file")
        if path.suffix not in ['.mp3', '.wav', '.ogv', '.mp4', '.flac']:
            raise ValueError("path does not point to an audio file")
        print(f"importing {path.name}...")

    def save():
        pass
    

if __name__ == "__main__":
    pass