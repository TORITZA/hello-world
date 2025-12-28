
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QV Box Layout Example")
        self.setFixedSize(400,300)

        layout = QVBoxLayout()

        layout.addWidget(Color("red"))
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

