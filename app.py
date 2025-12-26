
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

        self.setWindowTitle("QComboBox Demo")
        self.setFixedSize(400,300)
        
        combo = QComboBox()
        combo.addItems(["One", "Two", "Three"])

        # Sends the current index (position) of the selected item.
        combo.currentIndexChanged.connect(self.index_changed)

        # Alternate signal to send an option's text:
        combo.currentTextChanged.connect(self.text_changed)

        # Set QComboBox to be editable:
        # combo.setEditable(True)

        self.setCentralWidget(combo)
    
    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication([])


w = MainWindow()
w.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

