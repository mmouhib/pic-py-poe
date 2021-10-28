from singleplayer import Singleplayer
from multiplayer import Multiplayer
from multiplayer import Multiplayer
import loading
import result
import os


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


if __name__ == '__main__':
    print(result.title)
    print("""
    make your choice:
    (1) Single Player mode
    (2) Multi Player mode
    your choice => 
    """)

    while 1:
        choice = input()
        if choice in ('1', '2'):
            break

    loading.loading()
    clear_screen()

    if choice == '1':
        game = Singleplayer()
        game.main_game()

    else:
        game = Multiplayer()
        game.main_game()

    if game.result() == 0:
        pass

