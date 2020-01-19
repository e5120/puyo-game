from board import Board
from score import Score


def build_board(args, score, puyo_width=64, puyo_height=64):
    return Board(score,
                 puyo_width=puyo_width,
                 puyo_height=puyo_height,
                 vs=args.vs,
                 row=args.row,
                 column=args.column)


def build_score():
    return Score()


def build_puyo():
    pass
