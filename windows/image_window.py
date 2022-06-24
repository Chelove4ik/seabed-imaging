from PyQt5.QtWidgets import QMainWindow

from ui.image_view import Ui_MainWindow


class ImageWindow(QMainWindow):
    def __init__(self, array):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.array = array
        self.draw_image()

    def draw_image(self):
        pass
