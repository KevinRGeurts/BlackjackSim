class Card:
    """
    Represents a single card from a deck of playing cards.\n
    """
    
    def __init__(self, suit='H', pips='J'):
        """
        Construct a Card with given suit and pips.
            Suit: 'H' = Hearts, 'D' = Diamonds, 'S' = Spades, 'C' = Clubs
            Pips: 'A' = Ace, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J' = Jack, 'Q' = Queen, 'K' = King 
        count will be automatically set based on pips.
        """
        self.suit=suit
        self.pips=pips
        self.count=self.get_count_from_pips(pips)
        
    
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
    
    
    def __str__(self):
        return self.pips + self.suit
        
    
    # TODO: With __str__() implemented, this shouldn't be needed. Find all calls to it in the solution, update them to rely on str() or print()
    # and then delete this method.
    def print_card(self):
        """
        Returns a string representation of the card.
        :return: The string representing the card.
        """
        return str(self)
    
    
    def get_count_from_pips(self, pips=''):
        """
        Intended to be called by __init__(...) as a helper function to automatically determine the card count based on the pips.
        :parameter pips: A string representing the pips on a card (A, K, Q, J, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), str
        :return: The numeric count of the card, int 
        """
        card_count = 0
        if pips == 'A':
            card_count = 1
        elif pips == 'K' or pips == 'Q' or pips == 'J':
            card_count = 10
        else:
            card_count = int(pips)
        return card_count