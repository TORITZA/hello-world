
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nested Layouts Example")
        self.setFixedSize(400,300)

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color("purple"))
        layout2.addWidget(Color("pink"))
        layout2.addWidget(Color("blue"))

      # set spacing around the layout, no rim/border:
        layout1.setContentsMargins(0,0,0,0)
        # sets the spacing between elements:
        layout1.setSpacing(20)

        layout1.addLayout(layout2)

        layout1.addWidget(Color("red"))

        layout3.addWidget(Color("green"))
        layout3.addWidget(Color("yellow"))
        layout3.addWidget(Color("orange"))

        layout1.addLayout(layout3)
        
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

