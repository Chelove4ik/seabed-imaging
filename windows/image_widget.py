from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class Image(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image = None

    def initUI(self):
        self.show()

    def set_image(self, image):
        self.image = image

    def paintEvent(self, e):
        if self.image is None:
            return
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()
