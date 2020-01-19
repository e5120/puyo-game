from board import Board

def build_board(args, puyo_width=64, puyo_height=64):
    return Board(puyo_width=puyo_width,
                 puyo_height=puyo_height,
                 vs=args.vs,
                 row=args.row,
                 column=args.column)


def build_score():
    pass


def build_puyo():
    pass
