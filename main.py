import sys
from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from import_utils import ImportManager, import_widget
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("SimpleSample")
        self.setMinimumSize(QSize(500,500))

        self.import_manager = ImportManager(Path("./import.list"))

        layout = QVBoxLayout()
        audio_import_button = import_widget.Importer(self.import_manager)
        #button.setCheckable(True)
        layout.addWidget(audio_import_button)
        #layout.addWidget(Color('red'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        print("Tidying...")
        self.import_manager.tidy()
        self.import_manager.save()
        print("Done tidying.")
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()