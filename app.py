
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # variable to store the current state of a widget:
        self.button_is_checked = True 

        self.setWindowTitle('My App')

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        # Set central widget of the window: 
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        # .self reference required in order to access the button 
        # in this slot 
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)


app = QApplication([])

# Create a Qt Button widget, which automatically acts as the window: 
window = MainWindow()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

