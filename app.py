
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout Example")
        self.setFixedSize(400,300)

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 3)
        layout.addWidget(Color("pink"), 1, 1)
        layout.addWidget(Color("purple"), 2, 2)
        layout.addWidget(Color("blue"), 3, 0)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

