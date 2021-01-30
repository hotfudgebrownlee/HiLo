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
        self.player = Player()
        self.cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.old_card = 0
        
    def start_game(self):
        """
        
        """
        idx = random.randrange(0,13)
        self.old_card = self.cards[idx]
        while self.keep_playing:
            self.get_inputs()
            self.check_hilo()
            self.do_outputs()

    def get_inputs(self):
        """

        """
        print(f'The card is: {self.old_card}')
        self.player.hi_or_lo()

    def check_hilo(self):
        """
        """
        idx = random.randrange(0,13)
        print(f'Next card was: {self.cards[idx]}')
        if self.player.hilo == 'h':
            if self.cards[idx] > self.old_card:
                print(f'{self.cards[idx]} is higher than {self.old_card}.')
                self.player.score += 100
                print(f'Your score is: {self.player.score}')
            else:
                print(f'{self.cards[idx]} is not higher than {self.old_card}.')
                self.player.score -= 75
                print(f'Your score is: {self.player.score}')
        elif self.player.hilo == 'l':
            if self.cards[idx] < self.old_card:
                print(f'{self.cards[idx]} is lower than {self.old_card}.')
                self.player.score += 100
                print(f'Your score is: {self.player.score}')
            else:
                print(f'{self.cards[idx]} is not lower than {self.old_card}.')
                self.player.score -= 75
                print(f'Your score is: {self.player.score}')
        self.old_card = self.cards[idx]

    def do_outputs(self):
        """
        """
        if self.player.can_play():
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False