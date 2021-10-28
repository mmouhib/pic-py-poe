from singleplayer import Singleplayer
from multiplayer import Multiplayer
from multiplayer import Multiplayer
from colors import bcolors
import loading
import result
import os


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


if __name__ == '__main__':
    print(bcolors.HEADER + result.title + bcolors.ENDC)
    print("""
    make your choice:
    (1) Single Player mode
    (2) Multi Player mode
    """)

    while 1:
        choice = input('    your choice => ')
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
        print('Player 1: ')
        print(bcolors.OKBLUE + result.win + bcolors.ENDC)
    elif game.result() == 1:
        print('Player 1: ')
        print(bcolors.FAIL + result.loss + bcolors.ENDC)
    else:
        print(bcolors.OKGREEN + result.draw + bcolors.ENDC)
