
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QStackedLayout, 
    QWidget, 
    QGridLayout, 
    QVBoxLayout, 
    QHBoxLayout,
    QPushButton,
)

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStackedLayout Example")
        self.setFixedSize(400,300)

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout() 
        
        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stacklayout)

        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn_2 = QPushButton("green")
        btn_2.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn_2)
        self.stacklayout.addWidget(Color("green"))

        btn_3 = QPushButton("yellow")
        btn_3.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn_3)
        self.stacklayout.addWidget(Color("yellow"))
        
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

