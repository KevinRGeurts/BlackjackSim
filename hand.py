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
 
    
    def get_num_aces(self):
        """
        Return the number of aces in the Hand.
        :return: The integer number of aces in the Hand.
        """
        h = self.get_aces()
        return len(h.cards)
    
    
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

    
    def get_num_non_aces(self):
        """
        Return the number of cards that are not aces in the Hand.
        :return: The integer number of cards that are not aces in the Hand.
        """
        h = self.get_non_aces()
        return len(h.cards)


    def hand_info(self):
        """
        Return in a dictionary useful information for playing the hand in black jack.
            Num_Aces = How many cards in the hand are aces, int
            Num_Other = How many cards in the had are not aces, int
            Count_Other = Sum of the pip values of the cards that are not aces, int
        :return: A dictionary of useful information about the hand
        """
        info={}
        info['Num_Aces'] = self.get_num_aces()
        info['Num_Other'] = self.get_num_non_aces()
        info['Count_Other'] = self.get_non_aces().count_hand()
        return info
    

    def count_hand(self):
        """
        Count the hand.
        :return: The integer count value of the cards in the hand.
        """
        count = 0
        
        # TTD: Could use a lamda function maybe to compact this?
        for x in self.cards:
            count += x.count_card()
                
        return count
    
    def print_hand(self):
        """
        Returns a string representation of the hand.
        :return: The string representing the hand.
        """
        s = ''
        for x in self.cards:
            s += x.print_card() + ' '
        # Remove unneeded trailing space
        s = s[0:len(s)-1]
        return s
        