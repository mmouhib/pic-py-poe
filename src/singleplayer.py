import os
import random


class single_player:

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
        print('-' * 11)
        for sub_board in self.board:
            for sub_element in sub_board:
                print(sub_element, end=' | ')
            print()
            print('-' * 11)

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
        while 1:
            player_choice = self.player_choice()
            self.filler(player_choice, self.logo)
            if self.draw() or self.winner(self.logo) or self.winner(self.computer_logo):
                break
            computer_choice = self.computer_choice()
            self.filler(computer_choice, self.computer_logo)
            self.board_printer()

    def result(self):
        if self.winner(self.logo):
            print('player won')
        elif self.winner(self.computer_logo):
            print('computer won')
        else:
            print('draw')


game = single_player()
game.clear_screen()
game.main_game()
