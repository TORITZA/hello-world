
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        # Set central widget of the window: 
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print(f"Checked? {checked}")


app = QApplication([])

# Create a Qt Button widget, which automatically acts as the window: 
window = MainWindow()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

