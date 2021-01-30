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
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """

        """
        self.get_card()
        self.player.hi_or_lo()

    def get_card(self):
        """
        """
        idx = random.randrange(0,13)
        print(f'The card is: {self.cards[idx]}')
        self.old_card = self.cards[idx]

    def do_updates(self):
        """
        """
        idx = random.randrange(0,13)
        print(f'Next card was: {self.cards[idx]}')
        if self.player.hilo == 'h':
            if self.old_card > self.cards[idx]:
                print(f'{self.old_card} is higher than {self.cards[idx]}.')
                self.player.score += 100
                print(f'Your score is: {self.player.score}')
            else:
                print(f'{self.old_card} is not higher than {self.cards[idx]}.')
                self.player.score -= 75
                print(f'Your score is: {self.player.score}')
        elif self.player.hilo == 'l':
            if self.old_card < self.cards[idx]:
                print(f'{self.old_card} is lower than {self.cards[idx]}.')
                self.player.score += 100
                print(f'Your score is: {self.player.score}')
            else:
                print(f'{self.old_card} is not lower than {self.cards[idx]}.')
                self.player.score -= 75
                print(f'Your score is: {self.player.score}')
                
    def do_outputs(self):
        """
        """
        if self.player.can_play():
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False