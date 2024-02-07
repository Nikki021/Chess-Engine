# This file represents the basic outline of the chess board.

import chess
import chess.svg

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 900, 900)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(1, 1, 800, 800)

        self.chessboard = chess.Board()
        
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

board = chess.Board()
print(board)
print("\n\n")
board.push_san("e4")
print(board)
