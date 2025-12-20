from PyQt6.QtWidgets import QApplication, QWidget
# Only needed for access to command line arguments:
import sys

# You only need ONE QApplication instance per application.
# Pass in sys.argv to allow command line arguments for the app.
# If you know you won't use command line arguments, QApplication([]) works too.
app = QApplication([sys.argv])

# Create a Qt widget, which will be the window.
window = QWidget()
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Starts the event loop:
app.exec()


# The application won't breach this sector of code until exited, and the 
# event loop has stopped. 


