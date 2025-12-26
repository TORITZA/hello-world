
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

        self.setWindowTitle("QLineEdit Demo")
        self.setFixedSize(400,300)
        
        line = QLineEdit()
        line.setMaxLength(10)
        line.setPlaceholderText("Enter your text")

        #line.setReadOnly(True)

        # Perform input validation (IPv4 address example):
        #line.setInputMask('000.000.000.000;_')

        line.returnPressed.connect(self.return_pressed)
        line.selectionChanged.connect(self.selection_changed)
        line.textChanged.connect(self.text_changed)
        line.textEdited.connect(self.text_edited)

        self.setCentralWidget(line)
    
    def return_pressed(self):
        # User hits Enter:
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)
    
    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication([])


w = MainWindow()
w.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

