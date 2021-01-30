class Thrower:
    """
    
    """

    def __init__(self):
        """
        """
        self.score = 300
        self.hilo = ''

    def can_play(self):
        return (self.score > 0)

    def hi_or_lo(self):
        """
        """
        self.hilo = input("High or Low? [h/l] ")
        