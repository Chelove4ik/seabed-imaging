from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QSizePolicy

from mymath.mymath import function364, function43
from ui.image_view import Ui_MainWindow
from windows.image_widget import Image


class ImageWindow(QMainWindow):
    def __init__(self, array):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.array = array

        self.ui.w_log.hide()
        self.ui.rb_lin.clicked.connect(self.change_current_widget)
        self.ui.rb_log.clicked.connect(self.change_current_widget)

        self.ui.pb_draw.clicked.connect(self.draw_image)

        self.scene = QGraphicsScene()
        self.ui.gv_image.setScene(self.scene)

        self.ui.sa_image.setWidget(Image())

    def change_current_widget(self):
        if self.ui.rb_lin.isChecked():
            self.ui.w_log.hide()
            self.ui.w_lin.show()
        if self.ui.rb_log.isChecked():
            self.ui.w_lin.hide()
            self.ui.w_log.show()

    def draw_image(self):
        if self.ui.rb_lin.isChecked():
            image = function364(self.ui.sb_ld.value(), self.ui.sb_u.value(), self.array)
            image.save(f'lin_latest.png')

        if self.ui.rb_log.isChecked():
            image = function43(self.ui.sb_a.value(), self.array)
            image.save(f'log_latest.png')
        image = image.reduce(10)
        image = ImageQt(image)

        self.ui.sa_image.widget().set_image(image)
        self.ui.sa_image.widget().setGeometry(0, 0, image.size().width(), image.size().height())

        print("done paint")
