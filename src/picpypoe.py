#27-10-2021

"""
board printer
init board
valid choice checker
player choice
pc choice
gameover check:
	draw / loss / win

"""


import os
import random

def clrscr():
 	if os.name == 'posix':
 		os.system('clear')
 	else:
 		os.system('cls')
		

class game():
	def get_logo(self):
		while 1:
			self.logo = input('logo: ')
			if self.logo.upper() == 'X' or self.logo.upper() == 'O':
				break
			if self.logo.upper() == 'X':
				self.computer_logo = 'O'
			else:
				self.computer_logo = 'X'


	def get_name(self):
		self.name = input('name: ')

	def board_init(self):
		self.board = [
			['1', '2', '3'],
			['4', '5', '6'],
			['7', '8', '9']
		]

	def board_printer(self):
		print('-' * 11)
		for sub_board in self.board:
			for sub_element in sub_board:
				print(sub_element, end = ' | ')
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
			if self.check_valid_choice(self.board, choice):
				break
		return choice

	def player_choice(self):
		while 1:
			choice = input('')
			if self.check_valid_choice(self.board, choice):
				break
		return choice

	def filler(self, choice, logo):
		for x in range (3):
			for y in range(3):
				if self.board[x][y] == choice:
					self.board[x][y] = logo

clrscr()
game = game()
game.board_init()
game.board_printer()
print(game.check_valid_choice('0'))
