
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        # Set central widget of the window: 
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
       self.button.setText("You already clicked me.")
       self.button.setEnabled(False)

       # Also change the window title:
       self.setWindowTitle("My Oneshot App")


app = QApplication([])

# Create a Qt Button widget, which automatically acts as the window: 
window = MainWindow()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

