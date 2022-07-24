from board import Board
from iplayer import IPlayer


class Player(IPlayer):

    @property
    def trun(self):
        return "Ход игрока"

    def __init__(self):
        super().__init__(self)

