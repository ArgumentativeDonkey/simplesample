import subprocess
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QMessageBox, QPushButton, QVBoxLayout, QWidget

from import_utils import ImportManager


class TracklistButtons(QWidget):
    
    
    def __init__(self, import_manager: ImportManager):
        super().__init__()

        self.import_manager = import_manager

        layout = QVBoxLayout()

        self.refresh_button = QPushButton("🗘 Refresh Config")
        # self.refresh_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_BrowserReload))
        # self.refresh_button.setIconSize(QSize(24, 24))

        layout.addWidget(self.refresh_button)

        self.edit_button = QPushButton("✏️ Edit Config")
        # self.edit_button.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_CommandLink))
        # self.edit_button.setIconSize(QSize(24, 24))
        self.edit_button.clicked.connect(self.open_editor)

        layout.addWidget(self.edit_button)

        self.save_button = QPushButton("💾 Save")
        self.save_button.clicked.connect(self.save_config)

        layout.addWidget(self.save_button)

        self.autosave_cb = QCheckBox("Autosave Enabled")
        self.autosave_cb.setCheckState(Qt.CheckState.Checked if self.import_manager.autosave else Qt.CheckState.Unchecked)
        self.autosave_cb.toggled.connect(self.toggle_autosave)
        
        layout.addWidget(self.autosave_cb)

        self.setLayout(layout)

    def open_editor(self):
        if self.import_manager.storage_path is None:
            QMessageBox.critical(self, "Error", "No storage path set")
            return
        path = str(self.import_manager.storage_path.resolve().absolute())
    
        try:
            if sys.platform == "win32":
                subprocess.Popen(["notepad.exe", path])
    
            elif sys.platform == "darwin":
                subprocess.Popen(["open", "-e", path])
    
            else:
                subprocess.Popen(["xdg-open", path])
    
        except (FileNotFoundError, PermissionError, ValueError) as e:
            QMessageBox.critical(self, "Error", f"Could not open editor: {e}")
          

    def toggle_autosave(self, checked: bool):
        self.import_manager.autosave = checked

    def save_config(self):
        self.import_manager.save()
        