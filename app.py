
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

        self.setWindowTitle("QCheckBox Demo")
        self.setFixedSize(400,300)
        
        checkbox = QCheckBox("This is a checkbox!")
        checkbox.setCheckState(Qt.CheckState.Checked)

        # For tristate: checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)
    
    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)
        print(s)



app = QApplication([])


w = MainWindow()
w.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

