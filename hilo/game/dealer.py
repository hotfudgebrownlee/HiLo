from game.player import Player
import random

class Dealer:
    """
    
    """

    def __init__(self):
        """Class constructor. Declares/initializes attributes.

        Args:
        """
        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.old_card = 0
        
    def start_game(self):
        """
        
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """

        """
        self.get_card()
        self.player.

    def get_card(self):
        """
        """
        idx = random.randrange(0,13)
        print(f'Your card is {self.cards[idx]}.')
        self.old_card = self.cards[idx]