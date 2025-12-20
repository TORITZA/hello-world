# Only needed for access to command line arguments:
import sys
from PyQt6.QtWidgets import QApplication, QPushButton

# You only need ONE QApplication instance per application.
# Pass in sys.argv to allow command line arguments for the app.
# If you know you won't use command line arguments, QApplication([]) works too.
app = QApplication([sys.argv])

# Create a Qt Button widget, which automatically acts as the window.
window = QPushButton('Push me!')
window.show() # IMPORTANT!!!!!!!! Windows are hidden by default.

# Starts the event loop:
app.exec()


# The application won't breach this sector of code until exited, and the 
# event loop has stopped. 


