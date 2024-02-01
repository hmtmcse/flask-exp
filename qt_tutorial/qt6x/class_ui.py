import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class MyUI(QWidget):

    def __init__(self):
        super(MyUI, self).__init__()
        self.setWindowTitle("Example QT 6 UI")
        uic.loadUi('basic_ui.ui', self)
        self.show()


def run():
    app = QApplication(sys.argv)
    my_ui = MyUI()
    sys.exit(app.exec())


run()
