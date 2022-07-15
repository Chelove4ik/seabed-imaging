from PyQt5.QtWidgets import QMainWindow, QFileDialog

from iofile import read_file, fast_read_file
from ui.main import Ui_MainWindow
from windows.about_window import AboutWindow
from windows.help_window import HelpWindow
from windows.image_window import ImageWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.my_widget = None
        self.help_widget = HelpWindow()
        self.about_widget = AboutWindow()
        self.ui.pb_open.clicked.connect(self.open_file)
        self.ui.pb_help.clicked.connect(self.help_widget.show)
        self.ui.pb_about.clicked.connect(self.about_widget.show)

    def open_file(self):
        file = QFileDialog.getOpenFileName(self, "Выберите файл", filter='*.jsf *.txt *npy')

        try:
            arr = fast_read_file(file[0])  # select fast or normal file loader
        except Exception as e:
            print(e)
            return

        self.my_widget = ImageWindow(arr)
        self.my_widget.show()
