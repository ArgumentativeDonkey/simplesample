import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtMultimedia import QAudioDevice, QMediaPlayer, QPlaybackOptions
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QSlider,
    QStyle,
    QVBoxLayout,
    QWidget,
)

from import_utils import ImportManager


class TopBar(QFrame):
    def __init__(self):
        super().__init__()
        self.boxes = []
        bar_layout = QHBoxLayout(self)
        bar_layout.setContentsMargins(5,5,5,5)
        bar_layout.setSpacing(5)
        for i in range(5):
            box = self.AudioBox(i)
            self.boxes.append(box)
            bar_layout.addWidget(box, stretch=1)
    class AudioBox(QFrame):
        def __init__(self,index:int):
            super().__init__()
            self.setStyleSheet("QFrame { border: 1px solid #999; }")
            v_layout = QVBoxLayout(self)
            v_layout.setContentsMargins(4,4,4,4)
            v_layout.setSpacing(2)
            self.filename = QLabel("No file")
            self.playbackbutton = QPushButton("▶︎")
            self.volumeslider= QSlider(Qt.Orientation.Horizontal)
            self.volumeslider.setMaximum(200)
            self.volumeslider.setValue(100)
            self.volumelabel = QLabel(f"Volume ({self.volumeslider.value()}%)")
            self.volumeslider.valueChanged.connect(self.updateVolumeLabel)
            self.speedslider = QSlider(Qt.Orientation.Horizontal)
            self.speedslider.setMaximum(200)
            self.speedslider.setValue(100)
            self.speedlabel = QLabel(f"Speed ({self.speedslider.value()}%)")
            self.speedslider.valueChanged.connect(self.updateSpeedLabel)
            self.rewind = QPushButton("<-")
            self.fastforward = QPushButton("->")
            windlayout = QHBoxLayout()
            windlayout.setContentsMargins(4,4,2,2)
            windlayout.setSpacing(2)
            windlayout.addWidget(self.rewind)
            windlayout.addWidget(self.fastforward)
            winder = QWidget()
            winder.setLayout(windlayout)
            v_layout.addWidget(self.filename)
            v_layout.addWidget(self.playbackbutton)
            v_layout.addWidget(QLabel("Winder"), alignment=Qt.AlignmentFlag.AlignCenter)
            v_layout.addWidget(winder)
            v_layout.addWidget(self.volumelabel, alignment=Qt.AlignmentFlag.AlignCenter)
            v_layout.addWidget(self.volumeslider)
            v_layout.addWidget(self.speedlabel, alignment=Qt.AlignmentFlag.AlignCenter)
            v_layout.addWidget(self.speedslider)
        def updateVolumeLabel(self):
            self.volumelabel.setText(f"Volume ({self.volumeslider.value()}%)")
        def updateSpeedLabel(self):
            self.speedlabel.setText(f"Speed ({self.speedslider.value()}%)")
