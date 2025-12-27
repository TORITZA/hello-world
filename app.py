
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Widget")
        self.setFixedSize(400,300)
        
        widget = Color("red")
        self.setCentralWidget(widget)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

