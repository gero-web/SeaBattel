import random
from ii import Player_II
from player import Player

pii = Player_II()
pii.add_ships()
player = Player()
player.add_ships()
q = 'a'
player_trun = 1
players = [pii, player]
hit_playets = 0
print('Нажмите q для выхода!')
print("Поле ИИ")
pii.show_board_player(player)
print('--' * 10)
print('Поле игрока')
player.show_board_player(player)
while q != 'q':
    player_ = players[player_trun]
    try:
        hit = players[hit_playets]
        print('Нажмите q для выхода!')
        print("Поле ИИ")
        pii.show_board_player(player_)
        print('--' * 10)
        print('Поле игрока')
        player.show_board_player(player_)
        print(player_.trun)
        if isinstance(player_, Player):
            coord = input('Введите координаты, пример вода: х y:').split()
            if len(coord) == 2:
                if not all([x.isdigit() for x in coord]):
                    raise ValueError("Вы ввели не число!")
                x, y = map(int, coord)
            else:
                raise ValueError("Координат должно быть 2!")

        else:
            x, y = random.randint(1, 6), random.randint(1, 6)
        is_alive = hit.player_turn(x, y,hit)
        if is_alive:
            player_trun ^= 1
            hit_playets ^= 1
        else:
            print("Игра окончена!")
            if isinstance(player_, Player):
                print("Победил игрок!")
            else:
                print('Победил ИИ')
            pii.show_board_player(pii)
            player.show_board_player(player)
            break
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)
