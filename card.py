class Card:
    """
    Represents a single card from a deck of playing cards.\n
    """
    
    def __init__(self, suit='H', pips='J', count=10):
        """
        Construct a Card with given suit, pips, and count value
        """
        self.suit=suit
        self.pips=pips
        self.count=count
    
    def count_card(self, ace_high=False):
        """
        Return the numeric count of the card.
        :param ace_low: Should an ace be counted as 1 (False) or 11 (True)?
        :return: The numeric count of the card
        """
        card_count = 0;
        if (self.pips == 'A') and (ace_high):
            card_count = 11
        else:
            card_count = self.count
        return card_count
    
    def print_card(self):
        """
        Returns a string representation of the card.
        :return: The string representing the card.
        """
        return self.pips + self.suit