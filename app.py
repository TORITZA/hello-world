
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QCheckBox,
    QStatusBar,
    QToolBar
)


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QAction")
        self.setFixedSize(400,300)
       
        label = QLabel("hai! :3")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(label)

        toolbar = QToolBar("THE toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("My button", self)
        button_action.setStatusTip("This is MY button!")
        button_action.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(button_action)

    def toolbar_button_clicked(self, s):
        print("click", s)



app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

