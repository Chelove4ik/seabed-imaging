from PyQt5.QtWidgets import QMainWindow, QFileDialog

from iofile import read_file, fast_read_file
from ui.main import Ui_MainWindow
from windows.image_window import ImageWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.my_widget = None
        self.ui.pb_open.clicked.connect(self.open_file)

    def open_file(self):
        file = QFileDialog.getOpenFileName(self, "Выберите файл", filter='*.jsf *.txt *npy')

        try:
            arr = fast_read_file(file[0])  # select fast or normal file loader
        except Exception as e:
            print(e)
            return

        self.my_widget = ImageWindow(arr)
        self.close()
        self.my_widget.show()
