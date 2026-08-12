import sys

from PySide6.QtMultimedia import QMediaPlayer, QAudioDevice, QPlaybackOptions
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QVBoxLayout,
    QWidget, QPushButton,
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
            self.playbackbutton = QPushButton(">")
            v_layout.addWidget(self.filename)
            v_layout.addWidget(self.playbackbutton)
