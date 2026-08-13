
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSlider,
    QVBoxLayout,
    QWidget,
)

shortcuts = ['q', 'w', 'e', 'r', 't']

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
        def __init__(self, index:int):
            super().__init__()

            self.index = index
            
            self.setStyleSheet("QFrame { border: 1px solid #999; }")

            v_layout = QVBoxLayout(self)
            v_layout.setContentsMargins(4,4,4,4)
            v_layout.setSpacing(2)
            
            self.filename = QLabel(f"<b>{shortcuts[self.index].upper()}:</b> No file")
            
            self.playbackbutton = QPushButton("▶︎")
            
            self.volumeslider= QSlider(Qt.Orientation.Horizontal)
            self.volumeslider.setMaximum(200)
            self.volumeslider.setValue(100)
            
            self.volumelabel = QLabel(f"Volume ({self.volumeslider.value()}%)")
            self.volumeslider.valueChanged.connect(self.updateVolumeLabel)
            
            self.speedslider = QSlider(Qt.Orientation.Horizontal)
            self.speedslider.setMaximum(50)
            self.speedslider.setValue(10)
            self.speedslider.setMinimum(-50)
            self.speedslider.setTickInterval(10)
            
            self.speedlabel = QLabel(f"Speed ({self.speedslider.value() / 10}x)")
            self.speedslider.valueChanged.connect(self.updateSpeedLabel)

            self.speed_slider_reset = self.ResetButton("↻")
            self.speed_slider_reset.clicked.connect(self.reset_speed)

            self.upper_speed_layout = QHBoxLayout()
            self.upper_speed = QWidget()
            self.upper_speed.setLayout(self.upper_speed_layout)
            
            self.rewind = QPushButton("⏮")
            self.fastforward = QPushButton("⏩︎")
            
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

            self.upper_speed_layout.addWidget(self.speedlabel)
            self.upper_speed_layout.addWidget(self.speed_slider_reset)
            v_layout.addWidget(self.upper_speed, alignment=Qt.AlignmentFlag.AlignCenter)
            v_layout.addWidget(self.speedslider)
            
        def updateVolumeLabel(self):
            self.volumelabel.setText(f"Volume ({self.volumeslider.value()}%)")
            
        def updateSpeedLabel(self):
            self.speedlabel.setText(f"Speed ({self.speedslider.value() / 10}x)")

        def updateFileLabel(self):
            self.volumelabel.setText(f"")

        def reset_speed(self):
            self.speedslider.setValue(10)

        class ResetButton(QPushButton):
            def __init__(self, text, parent=None):
                super().__init__(text, parent)
                
                self.setMinimumSize(0, 0) 
                
                self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
                
                self.setStyleSheet("""
                    QPushButton {
                        border: 1px solid #999; /* Tiny border so you can see it */
                        padding: 0px;
                        margin: 0px;
                    }
                """)
        
            def resizeEvent(self, event):
                super().resizeEvent(event)
                label_height = self.fontMetrics().height()
                self.setFixedSize(label_height, label_height)

