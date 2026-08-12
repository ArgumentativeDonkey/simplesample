import subprocess
import sys
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

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

        self.setLayout(layout)

    def open_editor(self):
        abs_path = str(self.import_manager.storage_path)
        if sys.platform == "win32":
            subprocess.Popen(["notepad.exe", abs_path])
        elif sys.platform == "darwin": 
            subprocess.Popen(["open", "-e", abs_path])
        else: 
            try:
                subprocess.Popen(["gedit", abs_path])
            except FileNotFoundError:
                subprocess.Popen(["nano", abs_path])
        