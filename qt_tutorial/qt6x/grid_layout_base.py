import sys
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel


class GridLayoutBase(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('0,0'), 0, 0)
        grid.addWidget(QLabel('0,1'), 0, 1)
        grid.addWidget(QLabel('0,2'), 0, 2)
        grid.addWidget(QLabel('0,3'), 0, 3)
        grid.addWidget(QLabel('0,4'), 0, 4)
        grid.addWidget(QLabel('0,5'), 0, 5)

        grid.addWidget(QLabel('green'), 1, 0)
        grid.addWidget(QLabel('blue'), 1, 1)
        grid.addWidget(QLabel('purple'), 2, 1)

        self.move(300, 150)
        self.resize(800, 500)
        self.setWindowTitle('Calculator')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = GridLayoutBase()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


# https://www.pythontutorial.net/pyqt/pyqt-qgridlayout/