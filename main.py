from os import putenv
import sys

from PyQt5.QtWidgets import QApplication

import mymath.mymath
from iofile import read_file
from windows.main_window import MainWindow

if __name__ == '__main__':
    arr = read_file('data.txt')
    image = mymath.mymath.function364(10, arr)
    image.save('test.jpg', "JPEG")
    image.show()

    # app = QApplication(sys.argv)
    # w = MainWindow()
    # w.move(300, 300)
    # w.setFixedSize(700, 615)
    # w.setWindowTitle('Simple')
    # w.show()
    # sys.exit(app.exec_())
