import argparse
import sys

from PyQt5.QtWidgets import QApplication

from ui.utils import create_py_from_ui_folder, check_and_create_py_from_ui

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--recreate_uis', const=True)
    args = parser.parse_args()

    if args.recreate_uis is not None:
        create_py_from_ui_folder()
    else:
        check_and_create_py_from_ui()

    from windows.main_window import MainWindow

    app = QApplication(sys.argv)
    w = MainWindow()
    w.move(300, 300)
    w.setFixedSize(700, 615)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
