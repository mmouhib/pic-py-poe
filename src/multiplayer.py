from singleplayer import Singleplayer


class Multiplayer(Singleplayer):

    def player_choice(self, player):
        while 1:
            choice = input(f'{player} choice: ')
            if self.check_valid_choice(choice):
                break
        return choice

    def main_game(self):
        self.clear_screen()
        while 1:
            if self.draw() or self.winner(self.logo) or self.winner(self.computer_logo):
                break
            self.board_printer()
            player_one_choice = self.player_choice('player 1')
            self.filler(player_one_choice, self.logo)
            self.clear_screen()
            if self.draw() or self.winner(self.logo) or self.winner(self.computer_logo):
                break
            self.board_printer()
            player_two_choice = self.player_choice('player 2')
            self.filler(player_two_choice, self.computer_logo)
            self.clear_screen()
            self.board_printer()
            print(f'Player 1 choice: {player_one_choice}')
            print(f'Player 2 choice: {player_two_choice}')
            self.clear_screen()
