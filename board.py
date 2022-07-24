from ship import Ship


class Board:

    def __init__(self, n=7, m=7):
        self._n = n - 1
        self._m = m - 1
        self._new_board(n, m)

    def _new_board(self, n, m):
        self._board = [
            [i == 0 and j == 0 and 'y\\x' or i == 0 and j != 0 and j or j == 0 and i or 'O' for j in range(m)]
            for i in range(n)]

    @property
    def reshape(self):
        return self._new_board(self._n + 1, self._m + 1)

    def show(self, player_flag):
        for line in self._board:
            for cell in line:
                print(f"| {isinstance(cell, Ship) and cell.show(player_flag) or cell:<5} ", end='')
            print("|")

    def _border_board(self, ships):
        for deck in ships:
            n, m = deck.get_cord
            if (n >= 1 and m >= 1) and (n <= self._n and m <= self._m):
                return True
        return False

    # Как сделать эту часть более красивой более лучше , я не смог придумать нечго лучшего
    def _neighbor(self, ships, size):
        len_deck = 0
        for deck in ships:
            n, m = deck.get_cord
            c = - 1
            j = - 2
            k = 0
            if n == 6:
                k = 1
            if m == 6:
                j = -1

            while c < 2:

                i = (n - k) + c
                line = self._board[i][m - 1: m - j]
                result = all([not isinstance(item, Ship) for item in line])
                if not result:
                    return False
                if len_deck == 0 or size <= 1:
                    c += 1
                len_deck += 1
                size -= 1
        return True

    def _empty_field(self, ships):
        prev_coord = []
        for deck in ships:
            n, m = deck.get_cord
            if (not (n, m) in prev_coord) and self._board[n][m] == "O":
                prev_coord.append((n, m))
            else:
                return False
        return True

    def hit(self, n, m, player_flag):
        if (n >= 1 and m >= 1) and (n <= self._n and m <= self._m):
            if self._board[n][m] == "O":
                self._board[n][m] = "T"
            else:
                cell = self._board[n][m]
                if isinstance(cell, Ship):
                    cell.knocked_out = True
        else:
            raise IndexError("Вы вышли за пределы доски!")

        return self._count_ship_alive(player_flag)

    def _add_board(self, ships):
        for deck in ships:
            n, m = deck.get_cord
            self._board[n][m] = deck

    def _count_ship_alive(self, player_flag):
        count = 0
        for row in self._board:
            for column in row:
                ship = isinstance(column, Ship) and column
                if ship and ship.show(player_flag) == 'X':
                    count += 1

        if count >= 11:
            return False
        return True

    def put_cage(self, ships, size):
        if self._border_board(ships):
            if self._empty_field(ships):
                result = self._neighbor(ships, size)
                if result:
                    self._add_board(ships)
                    return True
                else:
                    return False
            else:
                raise ValueError("Клетка занята !")
        else:
            raise IndexError("Вы вышли за пределы доски")
    # --------------------------------------------------------------


if __name__ == '__main__':
    b = Board()

    ships = [Ship(4, 1), Ship(5, 5)]
    b.put_cage(ships, len(ships))
    ships = [Ship(4, 1), Ship(5, 2)]
    b.put_cage(ships, len(ships))
    b.show()

    print(b.shape)
    b.show()
