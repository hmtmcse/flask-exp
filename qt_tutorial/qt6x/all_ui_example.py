import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox


class AllUIExample(QWidget):
    def __init__(self):
        super(AllUIExample, self).__init__()
        self.setWindowTitle("All UI Example")
        self.button()
        self.show_dialog()

        self.resize(800, 500)
        self.make_window_center()
        self.show()

    def make_window_center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button(self):
        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(10, 20)

    def show_dialog(self):
        btn = QPushButton('Show Dialog', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.dialog_box)
        btn.move(10, 45)

    def dialog_box(self):
        response = QMessageBox.question(self, "Question dialog", "The longer message")
        if response == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")


def run():
    app = QApplication(sys.argv)
    my_ui = AllUIExample()
    sys.exit(app.exec())


run()
