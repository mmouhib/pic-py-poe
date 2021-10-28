import os
import random
from colors import bcolors


class Singleplayer:

    def __init__(self):
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        self.name = input('name: ')
        while 1:
            self.logo = input('logo: ')
            if self.logo.upper() == 'X' or self.logo.upper() == 'O':
                break
        self.logo = self.logo.upper()
        if self.logo == 'X':
            self.computer_logo = 'O'
        else:
            self.computer_logo = 'X'

    @staticmethod
    def clear_screen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def board_printer(self):
        print((bcolors.FAIL + '-' + bcolors.ENDC) * 13)
        for sub_board in self.board:
            print(bcolors.FAIL + '| ' + bcolors.ENDC, end='')
            for sub_element in sub_board:
                if sub_element == self.logo:
                    print(bcolors.OKBLUE + sub_element +
                          bcolors.ENDC, end=bcolors.FAIL + ' | ' + bcolors.ENDC)
                elif sub_element == self.computer_logo:
                    print(bcolors.WARNING + sub_element +
                          bcolors.ENDC, end=bcolors.FAIL + ' | ' + bcolors.ENDC)
                else:
                    print(sub_element, end=bcolors.FAIL + ' | ' + bcolors.ENDC)
            print()
            print((bcolors.FAIL + '-' + bcolors.ENDC) * 13)

    def check_valid_choice(self, choice):
        for sub_board in self.board:
            if choice in sub_board:
                return True
        return False

    def computer_choice(self):
        while 1:
            choice = random.randint(1, 9)
            choice = str(choice)
            if self.check_valid_choice(choice):
                break
        return choice

    def player_choice(self):
        while 1:
            choice = input('your choice: ')
            if self.check_valid_choice(choice):
                break
        return choice

    def filler(self, choice, logo):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == choice:
                    self.board[x][y] = logo

    def filled_board(self):
        for sub_board in self.board:
            for x in sub_board:
                if x.isdigit():
                    return False
        return True

    def winner(self, symbol):

        line_one = self.board[0]
        line_two = self.board[1]
        line_three = self.board[2]

        # Vertical
        if line_one[0] == line_two[0] == line_three[0] == symbol:
            return True
        elif line_one[1] == line_two[1] == line_three[1] == symbol:
            return True
        elif line_one[2] == line_two[2] == line_three[2] == symbol:
            return True
        # Horizontal
        elif line_one[0] == line_one[1] == line_one[2] == symbol:
            return True
        elif line_two[0] == line_two[1] == line_two[2] == symbol:
            return True
        elif line_three[0] == line_three[1] == line_three[2] == symbol:
            return True
        # diagonals
        elif line_one[0] == line_two[1] == line_three[2] == symbol:
            return True
        elif line_one[2] == line_two[1] == line_three[0] == symbol:
            return True
        return False

    def draw(self):
        if self.filled_board() and not (self.winner(self.logo) or self.winner(self.computer_logo)):
            return True
        return False

    def main_game(self):
        self.clear_screen()
        self.board_printer()
        while 1:
            if self.draw() or self.winner(self.logo) or self.winner(self.computer_logo):
                self.clear_screen()
                break
            player_choice = self.player_choice()
            self.filler(player_choice, self.logo)
            if self.draw() or self.winner(self.logo) or self.winner(self.computer_logo):
                self.clear_screen()
                break
            computer_choice = self.computer_choice()
            self.filler(computer_choice, self.computer_logo)
            self.clear_screen()
            self.board_printer()
            print(f'Player choice: {player_choice}')
            print(f'Computer choice: {computer_choice}')

    def result(self):
        if self.winner(self.logo):
            return 0
        elif self.winner(self.computer_logo):
            return 1
        return 2
