from pathlib import Path
from PySide6.QtWidgets import QWidget, QPushButton, QFileDialog, QVBoxLayout, QTreeView, QListView, QMessageBox, QCheckBox
from import_utils import ImportManager, SUPPORTED_AUDIO_FILES

MEDIA_FILTER = f"Media Files ({' '.join('*' + filetype for filetype in SUPPORTED_AUDIO_FILES)});;All Files (*)"

class MixedFileDialog(QFileDialog):
    def __init__(self, parent=None, caption="", directory="", filter_str=""):
        super().__init__(parent, caption, directory, filter_str)
         
        self.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        
        self.setFileMode(QFileDialog.FileMode.ExistingFiles)
        
        self.view = self.findChild(QTreeView) or self.findChild(QListView)

    def accept(self):
        """Forces the Open button to return selected folders instead of traversing them."""
        if self.view and self.view.selectionModel().hasSelection():
            super(QFileDialog, self).accept()
        else:
            super().accept()

class Importer(QWidget):
    def __init__(self, import_manager: ImportManager, autosave: bool = True):
        super().__init__()
        self.import_manager = import_manager
        self.autosave = autosave

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        import_audio_button = QPushButton("Import Audio")
        import_audio_button.setMinimumSize(100, 30)
        import_audio_button.clicked.connect(self.import_audio)

        layout.addWidget(import_audio_button)
     
    def import_audio(self):
        dialog = MixedFileDialog(self, "Select Files or Folders", filter_str=MEDIA_FILTER)

        if dialog.exec():
            selected_paths = [Path(file) for file in dialog.selectedFiles()]
            print(f"Selected: \n{selected_paths}")
            imported = 0
            skip_warnings = False
            for path in selected_paths:
                try:
                    imported += self.import_manager.import_path(path)
                except (ValueError, FileNotFoundError) as e:
                    if not skip_warnings:
                        msg = QMessageBox(self)
                        msg.setIcon(QMessageBox.Icon.Critical)
                        msg.setWindowTitle("Import Error")
                        msg.setText(f"Encountered an error importing {path.name}: {e}")
                        cb = QCheckBox("Ignore warnings for the rest of the files")
                        msg.setCheckBox(cb)
                        msg.exec()

                        if cb.isChecked():
                            skip_warnings = True
                        
            if self.autosave:
                self.import_manager.save()

            if imported:
                QMessageBox.information(self, "Imported Files", f"Imported {imported} {'file' if imported == 1 else 'files'}")
            else:
                QMessageBox.warning(self, "Imported Files", "No files were imported.")
        else:
            print("Cancelled operation.")