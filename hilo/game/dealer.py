from game.player import Player
import random

class Dealer:
    """A code template for the person dealing the cards and collecting
    bets. Keeps track of last card compared to new card. Awards or
    removes points depending on success of player guesses.

    Attributes:
        keep_playing (boolean): Whether or not the player wants
            to keep playing.
        cards (list of numbers): List of numbers 1 thru 13 that exist
            as possible outcomes when a card is flipped.
        old_card (number): a variable to store the previous number for
            comparison purposes.
        player (Player): an instance of the class of objects known as
            Player.    
    """

    def __init__(self):
        """Class constructor. Declares/initializes attributes.

        Args:
            self (Dealer): an instance of Dealer.
        """
        self.keep_playing = True
        self.cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.old_card = 0
        self.player = Player()
        
    def start_game(self):
        """Starts the game loop and controls sequence of play. Before
        initializing the game, picks the first card for gameplay.

        Args:
            self(Dealer): an instance of Dealer.
        Methods:
            get_inputs: displays card and allows player to choose
                high or low.
            check_hilo: checks if hilo guess was correct. Updates
                and displays score accordingly.
            keep_going: checks if user wants to keep playing and
                responds accordingly.
        """
        idx = random.randrange(0,13)
        self.old_card = self.cards[idx]
        while self.keep_playing:
            self.get_inputs()
            self.check_hilo()
            self.keep_going()

    def get_inputs(self):
        """Displays the value of the first card and calls the Player
        method which asks if the next card will be high or low.

        Args:
            self (Dealer): An instance of Dealer.
            player (Player): An instance of Player.
        """
        print(f'The card is: {self.old_card}')
        self.player.hi_or_lo()

    def check_hilo(self):
        """Checks the player's hilo guess and then checks the validity
        of the assertion by comparing the old card to the new one. Updates
        points accordingly and prints outputs. After this process, updates
        old_card in preparation for the next round.

        Args:
            self (Dealer): An instance of Dealer.
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

    def keep_going(self):
        """Calls on the player to see if they want to keep playing.
        Exits the game if false.

        Args:
            self (Dealer): An instance of Dealer.
            player (Player): An instance of Player.
        """
        if self.player.can_play():
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False