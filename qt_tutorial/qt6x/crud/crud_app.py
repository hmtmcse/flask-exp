import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView


class CRUDApp(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('crud.ui', self)
        self.show()
        self.load_table_data()
        self.addData.clicked.connect(self.save)

    def save(self):
        first_input = self.name.text()
        index = 10
        self.data_table.insertRow(index)
        self.data_table.setItem(index, 0, QTableWidgetItem(f"{index}"))
        self.data_table.setItem(index, 1, QTableWidgetItem(first_input))
        self.data_table.update()

    def load_table_data(self):
        self.data_table.verticalHeader().setVisible(False)
        header = self.data_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        for index in range(10):
            self.data_table.insertRow(index)
            self.data_table.setItem(index, 0, QTableWidgetItem(f"{index}"))
            self.data_table.setItem(index, 1, QTableWidgetItem(f"My Name is {index}"))
            self.data_table.setItem(index, 2, QTableWidgetItem(f"Mobile {index}"))
            self.data_table.setItem(index, 3, QTableWidgetItem(f"Email Address {index}"))
            self.data_table.update()


def run():
    app = QApplication(sys.argv)
    crud_app = CRUDApp()
    sys.exit(app.exec())


run()
