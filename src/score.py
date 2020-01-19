import numpy as np


class Score(object):
    def __init__(self):
        self.clear()

    def get_point(self, chain, attach, color):
        chain_bonus = self.chain_bonus(chain)
        attach_bonus = self.attach_bonus(attach)
        color_bonus = self.color_bonus(color)
        bonus = chain_bonus + attach_bonus + color_bonus
        bonus = bonus if bonus > 0 else 1
        self.total_score += bonus * 10
        return bonus * 10

    def chain_bonus(self, chain):
        if chain == 1:
            return 0
        elif 1 < chain < 6:
            return np.power(2, chain + 1)
        elif 6 <= chain <= 20:
            return 64 + 32 * (chain - 5)
        else:
            raise NotImplementedError()

    def attach_bonus(self, attach):
        if attach == 4:
            return 0
        elif 4 < attach < 11:
            return attach - 3
        elif 11 <= attach:
            return 10
        else:
            raise NotImplementedError()

    def color_bonus(self, color):
        if color == 1:
            return 0
        elif 1 < color <= 5:
            return 3 * np.power(2, color - 2)
        else:
            raise NotImplementedError()

    def clear(self):
        self.total_score = 0
