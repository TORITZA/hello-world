
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox
    )


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSlider Demo")
        self.setFixedSize(400,300)
        
        slider = QSlider(Qt.Orientation.Horizontal)

        slider.setMinimum(-10)
        slider.setMaximum(3)
        # Or: spin.setRange(-10, 3)

        slider.setSingleStep(3)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(slider)
    
    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("Position", p)
    
    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication([])


w = MainWindow()
w.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

