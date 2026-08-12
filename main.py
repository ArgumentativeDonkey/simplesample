from pathlib import Path
from layout_colorwidget import Color
from import_utils import import_widget, ImportManager
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("SimpleSample")
        self.setMinimumSize(QSize(500,500))

        self.import_manager = ImportManager(Path("./import.list"))

        print("Tidying...")
        self.import_manager.tidy()
        self.import_manager.save()
        print("Done tidying.")

        layout = QVBoxLayout()
        audio_import_button = import_widget.Importer(self.import_manager)
        #button.setCheckable(True)
        layout.addWidget(audio_import_button)
        #layout.addWidget(Color('red'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()