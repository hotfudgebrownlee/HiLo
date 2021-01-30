class Player:
    """A code template for a person who picks cards. The responsibility
    of this class of objects is to guess whether the next card will
    higher or lower than the last, and also check if the score is above
    zero.
    
    Attributes:
        score (number): the initial score that will be changed by the
            dealer based on success of guesses.
        hilo (string): the user guess as to whether the next card will be
            higher or lower than the last.
    """

    def __init__(self):
        """Class constructor. Declares/initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.score = 300
        self.hilo = ''

    def can_play(self):
        """Determines whether or not the Player can guess again based
        on the score. If the score is below zero, this method returns
        false.

        Args:
            self (Player): An instance of Player.

        Returns:
            boolean: True if the score is greater than 0, false if less.
        """
        return (self.score > 0)

    def hi_or_lo(self):
        """Gets input from the user determining if the next card will be
        higher or lower than the last.

        Args:
            self (Player): An instance of Player.
        """
        self.hilo = input("High or Low? [h/l] ")
        