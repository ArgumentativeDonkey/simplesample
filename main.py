import sys
from pathlib import Path

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from import_utils import ImportManager, import_widget
from layout_colorwidget import Color
from mainmanager import TopBar
from tracklist import TrackList


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimpleSample")
        self.setFixedSize(QSize(1300, 700))

        self.import_manager = ImportManager(Path("./import.list"))
        print("Tidying...")
        self.import_manager.tidy()
        self.import_manager.save()
        print("Done tidying.")
        audio_import_button = import_widget.Importer(self.import_manager)
        audio_import_button.setFixedSize(QSize(140, 50))
        self.tracklist = TrackList(self.import_manager)
        self.tracklist.setFixedSize(300, 600)
        self.import_manager.new_paths.connect(self.tracklist.add_paths)
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.addWidget(audio_import_button, alignment=Qt.AlignmentFlag.AlignTop)
        left_layout.addWidget(self.tracklist, alignment=Qt.AlignmentFlag.AlignTop)
        left_layout.addStretch()
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 70, 0, 0)
        self.top_bar = TopBar()
        right_layout.addWidget(self.top_bar)
        right_layout.addStretch()
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget, stretch=1)
        central = QWidget()
        central.setLayout(main_layout)
        self.setCentralWidget(central)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
