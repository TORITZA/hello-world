
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

        self.setWindowTitle("QListWidget Demo")
        self.setFixedSize(400,300)
        
        list_w = QListWidget()
        list_w.addItems(["One", "Two", "Three"])

        list_w.currentItemChanged.connect(self.item_changed)
        list_w.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(list_w)
    
    def item_changed(self, i): # NOT an index; is a QListWidgetItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication([])


w = MainWindow()
w.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

