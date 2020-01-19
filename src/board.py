from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Board(QWidget):
    def __init__(self, score, parent=None, puyo_width=16, puyo_height=16,
                 column=6, row=13, vs=False):
        super(Board, self).__init__(parent)

        self.score = score
        self.column = column
        self.row = row
        width = column * puyo_width + 50
        height = row * puyo_height + 50
        if vs:
            width = width * 2 + 100
        self.setGeometry(300, 50, width, height)
        self.setWindowTitle('Puyo-Puyo')
