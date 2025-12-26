
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
        
        dial = QDial()
        dial.setRange(-10, 100)
        dial.setSingleStep(1)

        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.slider_position)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(dial)
    
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

