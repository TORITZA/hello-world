from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QCheckBox,
    QStatusBar,
    QToolBar,
    QDialog,
    QWidget,
    QDialogButtonBox,
    QVBoxLayout
)
from random import randint


class AnotherWindow(QWidget):
    '''
    This window is a QWidget. Without a parent, it will appear as 
    a free-floating window.
    '''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(f"window {randint(0, 100)}")
        layout.addWidget(self.label)
        self.setFixedSize(QSize(300,200))
        self.setLayout(layout)


# CUSTOM DIALOG BOX:
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HI.")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        layout = QVBoxLayout()
        message = QLabel("...Something just happened.")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


