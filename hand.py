from card import Card

class Hand:
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
        Add a list of one or more new Card(s), or a single Card to the hand.
        :param newCards: The lisf of new Card(s), or a single Card to be added to the hand
        :return: A list of the cards in the hand.
        """
        if type(newCards) == type(Card()):
            self.cards.append(newCards)
        elif type(newCards) == type([]):  
            self.cards.extend(newCards)
        return self.cards
    
    
    def get_aces(self):
        """
        Return a new Hand of only the aces in the Hand.
        :return: A Hand of aces in the Hand.
        """
        # Extract the list of any aces in the hand.
        # Do the extraction using a "list comprehension"
        aces=[x for x in self.cards if x.get_pips() == 'A']
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
        non_aces=[x for x in self.cards if x.get_pips() != 'A']
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
    
   
    def get_num_cards(self):
        """
        Return the total number of cards in the Hand. By convention, this method should be used, rather than 
        directly accessing the Hand's cards data member and using len(), to insulate the outside world from the details Hand's data model.
        "return: Total number of cards in the hand, int
        """
        return len(self.cards)
    
    
    # TODO: Determine if the return is a copy of the list of cards or if it is returning a reference to the internal list
    # of cards, since the later would allow corruption of the internal data store and by convention should be avoided.
    def get_cards(self):
        """
        Return a list of the cards in the Hand. By convention, this method should be used, rather than 
        directly accessing the Hand's cards data member, to insulate the outside world from the details Hand's data model.
        "return: Cards in the hand, list
        """
        return self.cards


    def hand_info(self):
        """
        Return in a dictionary of useful information for playing the hand in black jack.
            Num_Aces = How many cards in the hand are aces, int
            Num_Other = How many cards in the had are not aces, int
            Count_Other = Sum of the pip values of the cards that are not aces, int
            Count_Min = Sum of the pip values of all the cards, treating any aces as having 1 pip, int
            Count_Max = Sum of the pip values of all the cards, treating the first ace as having 11 pips, and any remaining
                as having 1 pip, int
        :return: A dictionary of useful information about the hand
        """
        info={}
        num_aces = self.get_num_aces()
        info['Num_Aces'] = num_aces
        info['Num_Other'] = self.get_num_non_aces()
        info['Count_Other'] = self.get_non_aces().count_hand()
        
        # Determine Count_Min
        # Count all aces in the hand has "low", that is, having 1 pip.
        info['Count_Min'] = self.count_hand()
        
        # Determine Count_Max
        # Count aces in the hand. The first ace if any will be counted as "high" (i.e. 11), while any remaining will be counted as "low" (i.e. 1)
        # This is based on the logic that two (or more) aces all counted "high" will allways bust the hand.
        count_aces = 0
        if num_aces > 0:
            # There is at least one ace. Add one ace counted "high" (i.e. 11) to the count value of aces in the hand
            count_aces += self.get_aces().cards[0].count_card(ace_high=True)
        if (num_aces - 1) > 0:
            # There is more than one ace. Add a "low" (i.e. 1) ace value to the count value of aces in the hand for each ace beyond one
            count_aces += (num_aces - 1) * self.get_aces().cards[0].count_card(ace_high=False)
        info['Count_Max'] = info['Count_Other'] + count_aces

        return info
    

    def count_hand(self):
        """
        Count the hand, with any aces treated as "low".
        :return: The integer count value of the cards in the hand.
        """
        count = 0
        
        # TODO: Could use a lamda function maybe to compact this?
        for x in self.cards:
            count += x.count_card(ace_high=False)
                
        return count
    
    
    def __str__(self):
        s = ''
        for x in self.cards:
            s += str(x) + ' '
        # Remove unneeded trailing space
        s = s[0:len(s)-1]
        return s       

        