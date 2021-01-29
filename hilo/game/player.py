class Thrower:
    """
    
    """

    def __init__(self):
        """
        """
        self.score = 300

    def can_play(self):
        return (self.score > 0)

    def hi_or_lo(self):
        """
        """
        choice = input("High or Low? [h/l]")
        