from singleplayer import Singleplayer


class Multiplayer(Singleplayer):
    def __init__(self):
        super().__init__()
        self.name_two = input('name: ')

    def main_game(self):
        while 1:
            player_one_choice = self.player_choice()
            self.filler(player_one_choice, self.logo)
            if self.draw() or self.winner(self.logo) or self.winner(self.computer_logo):
                break
            player_two_choice = self.player_choice()
            self.filler(player_two_choice, self.computer_logo)
            self.board_printer()
