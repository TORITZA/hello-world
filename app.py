
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QVBoxLayout



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set central widget of the window: 
        self.setCentralWidget(container)



app = QApplication([])

# Create a Qt Button widget, which automatically acts as the window: 
window = MainWindow()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Start the event loop:
app.exec()

