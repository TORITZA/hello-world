
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    'My App', 
    'My App', 
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0 

        self.setWindowTitle('My App')

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Set central widget of the window: 
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        # self.windowTitleChanged passes in current (previously altered)
        # window title to this function
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication([])

# Create a Qt Button widget, which automatically acts as the window: 
window = MainWindow()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

