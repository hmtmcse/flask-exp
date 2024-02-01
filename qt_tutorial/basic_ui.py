from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('basic_ui.ui', self)  # Load the .ui file

        self.calculateButton.clicked.connect(self.click_on_calculate_button)

        self.show()

    def click_on_calculate_button(self):
        first_input = self.firstInput.text()
        second_input = self.secondInput.text()
        self.resultLabel.setText(f"{int(first_input) + int(second_input)}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
