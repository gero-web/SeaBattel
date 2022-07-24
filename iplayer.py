import math
from abc import abstractproperty, abstractmethod
from board import Board
import random

from ship import Ship


class IPlayer:

    def __init__(self, player_flag):
        self.ships_count = {1: 4, 2: 2, 3: 1}
        self._hit_was = []
        self.good_coord = []
        self.bad_coord = []
        self.board = Board()
        self.player_flag = player_flag

    def _rand_coord(self, n=6, m=6):
        n_rand = random.randint(1, n)
        m_rand = random.randint(1, m)
        return n_rand, m_rand

    def _new_coord(self, ship):

        if not ship:
            n_rand, m_rand = self._rand_coord()
            return n_rand, m_rand

        while True:
            n_rand, m_rand = self._rand_coord()
            n, m = ship[0].get_cord
            n0, m0 = ship[-1].get_cord
            distance = (n - n_rand) ** 2 + (m - m_rand) ** 2
            distance = math.sqrt(distance)
            if distance == 1:
                if ((m - m_rand) == 0 and (m0 - m_rand) == 0 and m - m0 == 0) or (
                        (n - n_rand) == 0 and (n0 - n_rand) == 0 and n - n0 == 0):
                    return n_rand, m_rand

    def add_ships(self):
        size = 1
        result = False
        while size < 4:
            not_zero = self.ships_count[size] > 0
            if not not_zero:
                size += 1
                continue
            ship = []
            for _ in range(size):
                n_rand, m_rand = self._new_coord(ship)
                ship.append(Ship(n_rand, m_rand, self.player_flag))
            try:
                result = self.board.put_cage(ship, size)

            except ValueError as e:
                for deck in ship:
                    self.bad_coord.append(deck.get_cord)
                if len(self.bad_coord) > 400:
                    break

            if result:
                result = False
                self.ships_count[size] -= 1
                self.bad_coord = []
                not_zero = self.ships_count[size] > 0
                if not not_zero:
                    size += 1

        remainder = any(self.ships_count.values())
        if remainder:
            self._restart()
            return None

    def show_board_player(self, player_flag):
        self.board.show(player_flag)

    def _restart(self):
        self.ships_count = {1: 4, 2: 2, 3: 1}
        self.bad_coord = []
        self.good_coord = []
        self.board = Board()
        self.add_ships()

    @abstractmethod
    def trun(self):
        pass

    def player_turn(self, n, m, player_flag):
        if (n, m) not in self._hit_was:
            self._hit_was.append((n, m))
            return self.board.hit(n, m, player_flag)
        else:
            raise ValueError("Ход уде был!!")
