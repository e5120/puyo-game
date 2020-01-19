import sys
import argparse

import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from builder import build_score, build_board, build_puyo
import opts


def main(args):
    app = QApplication(sys.argv)
    main_window = build_board(args,
                              puyo_width=64,
                              puyo_height=64)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Puyo-Puyo Games")

    opts.game_opts(parser)
    opts.log_opts(parser)

    args = parser.parse_args()

    main(args)
