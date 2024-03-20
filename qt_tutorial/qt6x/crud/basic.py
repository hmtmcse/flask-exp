import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class Basic(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('crud.ui', self)
        self.show()


def run():
    app = QApplication(sys.argv)
    ui_app = Basic()
    sys.exit(app.exec())


run()
