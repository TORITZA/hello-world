
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
    QMessageBox
)
from subclass_module import CustomDialog


# Subclass QMainWindow to customize the app's main window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDialog Demo")
        self.setFixedSize(400,300)
       
        label = QLabel("hai! :3")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(label)

        toolbar = QToolBar("THE toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("animal.png"),"My button", self)
        button_action.setStatusTip("This is MY button!")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence('Ctrl+p'))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("animal-dog.png"), "My SECOND button", self)
        button_action2.setStatusTip("This is my SECOND button!!")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel("do u like?"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&file")
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("submenu")
        file_submenu.addAction(button_action2)


        # DIALOG BOX:
        toolbar.addSeparator()

        button = "press 4 dialog!"
        dialog_button = QAction(button, self)
        dialog_button.setStatusTip("dialog box")
        dialog_button.triggered.connect(self.dialog_getter)
        toolbar.addAction(dialog_button)

        # MESSAGE BOX: 
        time_icon = "alarm-clock--exclamation.png"
        time_btn = QAction(QIcon(time_icon), "message pop-up", self)
        time_btn.setStatusTip("message box")
        time_btn.triggered.connect(self.message_getter)
        toolbar.addAction(time_btn)

        file_menu.addSeparator()
        file_menu.addAction(time_btn)


    def toolbar_button_clicked(self, s):
        print("click", s)

    def dialog_getter(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec():
            print("Yippie! Success!")
        else:
            print("Cancelled!")
    
    def message_getter(self, s):
        msg = QMessageBox(self)
        msg.setWindowTitle("hey, you!")
        msg.setText("Time's up!")
        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        msg.setIcon(QMessageBox.Icon.Warning)
        button = msg.exec()

        if button == QMessageBox.StandardButton.Close:
            print("hey, don't ignore me!!")



app = QApplication([])
w = MainWindow()
w.show() 

# Start the event loop:
app.exec()

