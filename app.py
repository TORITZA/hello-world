from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

# Subclass QMainWindow to customize app's main window
# **Allows the window behavior to be self-contained 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        button = QPushButton('Press me!')

    # Set the central widget of the window:
        self.setCentralWidget(button)
        # By default, takes the whole of the window.


app = QApplication([])

# Create a Qt Button widget, which automatically acts as the window.
window = MainWindow()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

