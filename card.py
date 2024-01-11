class Card:
    """
    Represents a single card from a deck of playing cards.\n
    """
    
    # TODO: Add a way to construct a card such that count is automatically set based on pips, to mitigate the risk
    # of inconsistency (done). Update as needed through the solution construction of cards to use this new method (not done).
    # One option would be to default count to 0, and if count is 0 then set it based on pips (done). This would I think keep all existing
    # card constructions working without issue, until they could be updated.
    def __init__(self, suit='H', pips='J', count=0):
        """
        Construct a Card with given suit, pips, and count value.
        If count=0 (the default), then count will be automatically set based on pips.
        """
        self.suit=suit
        self.pips=pips
        # self.count=count
        if count == 0:
            self.count=self.get_count_from_pips(pips)
        else:
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