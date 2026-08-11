from PySide6.QtCore import QSize, Qt #type: ignore
from PySide6.QtWidgets import ( #type:ignore
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimpleSample")
        self.setMinimumSize(QSize(1400,800))
        layout = QVBoxLayout()
        audioUploadB = QPushButton("Upload audio")
        audioUploadB.setFixedSize(QSize(100,30))
        #button.setCheckable(True)
        audioUploadB.clicked.connect(self.uploadAudio)
        layout.addWidget(audioUploadB)
        layout.addWidget(Color('red'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def uploadAudio(self):
        print("test")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()