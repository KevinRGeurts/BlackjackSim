from card import Card

class Hand(object):
    """
    Represents a hand of playing cards.\n
    """


    def __init__(self):
        """
        Construct an empty hand of playing cards.
        """
        # List of cards in the hand
        self.cards=[]

    
    def add_cards(self, newCards=[]):
        """
        Add a list of one or more new Card(s) to the hand.
        :param newCards: The lisf of new Card(s) to be added to the hand
        :return: A list of the cards in the hand.
        """
        self.cards.extend(newCards)
        return self.cards
    
    
    def get_aces(self):
        """
        Return a new Hand of only the aces in the Hand.
        :return: A Hand of aces in the Hand.
        """
        # Extract the list of any aces in the hand.
        # Do the extraction using a "list comprehension"
        aces=[x for x in self.cards if x.pips == 'A']
        ah = Hand()
        ah.add_cards(aces)
        return ah
    
    
    def get_non_aces(self):
        """
        Return a new Hand of only the non ace cards in the Hand.
        :return: A Hand of non ace cards in the Hand.
        """
        # Extract the list of any aces in the hand.
        # Do the extraction using a "list comprehension"
        non_aces=[x for x in self.cards if x.pips != 'A']
        h = Hand()
        h.add_cards(non_aces)
        return h


    def count_hand(self):
        """
        Count the hand using black jack rules.
        :return: The integer count value of the cards in the hand.
        """
        count = 0
        # Extract the list of any aces in the hand, since they must be counted as high or low depending on the other cards in the hand
        # Do the extraction using a "list comprehension"
        aces=[x for x in self.cards if x.pips == 'A']
        # Extract the list of non ace cards in the hand
        other=[x for x in self.cards if x.pips != 'A']
        # Count the non ace cards in the hand
        for x in other:
            count += x.count_card()
        
        # Count any aces in the hand to keep the total count of all cards <= 21
        for  x in aces:
            if count <= (21-11):
                count += x.count_card(ace_high = True)
        
        
        return count
        