
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QStackedLayout, 
    QWidget, 
    QGridLayout, 
    QVBoxLayout, 
    QHBoxLayout,
    QPushButton,
    QTabWidget
)

from layout_colorwidget import Color


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget Example")
        self.setFixedSize(400,300)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)
       

app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

