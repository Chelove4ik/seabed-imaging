from PyQt5.QtWidgets import QMainWindow

from ui.about import Ui_MainWindow


class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.back_button.clicked.connect(self.close)
