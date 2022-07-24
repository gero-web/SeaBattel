class Ship:

    def __init__(self, n, m, player_flag):
        self._n = n
        self._m = m
        self.knocked_out = False
        self.player_flag = player_flag

    @property
    def get_cord(self):
        return self._n, self._m

    def show(self, player_flag):
        if self.knocked_out:
            return 'X'
        if player_flag == self.player_flag:
            return '■'
        return 'O'
