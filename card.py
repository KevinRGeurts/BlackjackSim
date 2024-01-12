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

    def get_pips(self):
        """
        Return the Card's pips as a string. By convention, this method should be used to get a Card's pips, rather than 
        directly accessing the pips data member, to insulate the outside world from the details Card's data model.
        "return: Card's pips, string
        """
        return self.pips
    

    def get_suit(self):
        """
        Return the Card's suit as a string. By convention, this method should be used to get a Card's suit, rather than 
        directly accessing the suit data member, to insulate the outside world from the details Card's data model.
        "return: Card's suit, string
        """
        return self.suit