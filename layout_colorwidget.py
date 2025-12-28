
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color: str):
        super().__init__()
        
        # automatically fills its background w/ window color
        self.setAutoFillBackground(True)

        palette = self.palette()
        
        # change current window color to new, passed-in QColor:
        palette.setColor(QPalette.ColorRole.Window, QColor(color))

        # apply new color value back to custom widget:
        self.setPalette(palette)



