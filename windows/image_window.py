from PyQt5.QtWidgets import QMainWindow

from ui.image_view import Ui_MainWindow


class ImageWindow(QMainWindow):
    def __init__(self, array):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.array = array
        self.draw_image()

        self.ui.w_log.hide()
        self.ui.rb_lin.clicked.connect(self.change_current_widget)
        self.ui.rb_log.clicked.connect(self.change_current_widget)

    def change_current_widget(self):
        if self.ui.rb_lin.isChecked():
            self.ui.w_log.hide()
            self.ui.w_lin.show()
        if self.ui.rb_log.isChecked():
            self.ui.w_lin.hide()
            self.ui.w_log.show()

    def draw_image(self):
        pass
