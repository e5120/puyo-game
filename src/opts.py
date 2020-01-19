def game_opts(parser):
    parser.add_argument("--vs", action="store_true")
    parser.add_argument("--row", type=int, default=13)
    parser.add_argument("--column", type=int, default=6)


def log_opts(parser):
    pass
