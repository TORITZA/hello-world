
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

        self.setWindowTitle("Q(Double)SpinBox Demo")
        self.setFixedSize(400,300)
        
        spin = QSpinBox()
        # Or: spin = QDoubleSpinBox()

        spin.setMinimum(-9)
        spin.setMaximum(3)
        # Or: spin.setRange(-9, 3)

        spin.setPrefix("$")
        spin.setSuffix("c")
        spin.setSingleStep(3) # Or 3.0 for QDoubleSpinBox
        spin.valueChanged.connect(self.value_changed)
        spin.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(spin)
    
    def value_changed(self, i):
        print(i)

    def value_changed_str(self ,s):
        print(s)


app = QApplication([])


w = MainWindow()
w.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

