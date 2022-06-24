from os import putenv
import sys

from PyQt5.QtWidgets import QApplication

from windows.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.move(300, 300)
    w.setFixedSize(700, 615)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
