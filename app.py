
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QV Box Layout Example")
        self.setFixedSize(400,300)

        layout = QHBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("pink"))
        layout.addWidget(Color("purple"))
        layout.addWidget(Color("blue"))
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

