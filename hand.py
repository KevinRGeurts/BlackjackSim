# Local
from card import Card

class HandInfo:
    """
    This class is a structured way of returning information from Hand.hand_info(). Think of this as a C struct, where it is
    expected that data members will be direcly accessed, because this class has no methods, beyound __init__().
    """
    def __init__(self):
        """
        Create the data members of structured info.
            Num_Aces = How many cards in the hand are aces, int
            Num_Other = How many cards in the had are not aces, int
            Count_Other = Sum of the pip values of the cards that are not aces, int
            Count_Min = Sum of the pip values of all the cards, treating any aces as having 1 pip, int
            Count_Max = Sum of the pip values of all the cards, treating the first ace as having 11 pips, and any remaining
                as having 1 pip, int
        """
        self.Num_Aces = 0
        self.Num_Other = 0
        self.Count_Other = 0
        self.Count_Min = 0
        self.Count_Max = 0
        self.String_Rep = ''
        
    
    def __str__(self):
        s = 'String_rep = ' + self.String_Rep + 'Num_Aces = ' + str(self.Num_Aces) + ' Num_Other = ' + str(self.Num_Other) + ' Count_Other = ' + str(self.Count_Other) + ' Count_Min = ' + str(self.Count_Min) + ' Count_Max = ' + str(self.Count_Max)
        return s


class Hand:
    """
    Represents a hand of playing cards.\n
    """


    def __init__(self):
        """
        Construct an empty hand of playing cards.
        """
        # List of cards in the hand
        self._cards=[]

    
    def add_cards(self, newCards=[]):
        """
        Add a list of one or more new Card(s), or a single Card to the hand.
        :param newCards: The lisf of new Card(s), or a single Card to be added to the hand
        :return: A list of the cards in the hand, a shallow copy of self._cards, list
        """
        if type(newCards) == type(Card()):
            self._cards.append(newCards)
        elif type(newCards) == type([]):  
            self._cards.extend(newCards)
        return list(self._cards) # list(list) makes a shallow copy, which is what we want
    
    
    def get_aces(self):
        """
        Return a new Hand of only the aces in the Hand.
        :return: A Hand of aces in the Hand.
        """
        # Extract the list of any aces in the hand.
        # Do the extraction using a "list comprehension"
        aces=[x for x in self._cards if x.get_pips() == 'A']
        ah = Hand()
        ah.add_cards(aces)
        return ah
 
    
    def get_num_aces(self):
        """
        Return the number of aces in the Hand.
        :return: The integer number of aces in the Hand.
        """
        h = self.get_aces()
        return h.get_num_cards()
    
    
    def get_non_aces(self):
        """
        Return a new Hand of only the non ace cards in the Hand.
        :return: A Hand of non ace cards in the Hand.
        """
        # Extract the list of any aces in the hand.
        # Do the extraction using a "list comprehension"
        non_aces=[x for x in self._cards if x.get_pips() != 'A']
        h = Hand()
        h.add_cards(non_aces)
        return h

    
    def get_num_non_aces(self):
        """
        Return the number of cards that are not aces in the Hand.
        :return: The integer number of cards that are not aces in the Hand.
        """
        h = self.get_non_aces()
        return h.get_num_cards()
    
   
    def get_num_cards(self):
        """
        Return the total number of cards in the Hand. By convention, this method should be used, rather than 
        directly accessing the Hand's _cards data member and using len(), to insulate the outside world from the details Hand's data model.
        "return: Total number of cards in the hand, int
        """
        return len(self._cards)
    
    
    def get_cards(self):
        """
        Return a list of the cards in the Hand. By convention, this method should be used, rather than 
        directly accessing the Hand's cards data member, to insulate the outside world from the details Hand's data model.
        :return: Cards in the hand, a shallow copy of self._cards, list
        """
        return list(self._cards) # list(list) makes a shallow copy, which is what we want

 
    def hand_info(self):
        """
        Return a HandInfo object, with useful information for playing the hand in black jack.
        :return: A HandInfo object of useful information about the hand
        """
        info=HandInfo()
        info.String_Rep = str(self)
        num_aces = self.get_num_aces()
        info.Num_Aces = num_aces
        info.Num_Other = self.get_num_non_aces()
        info.Count_Other = self.get_non_aces().count_hand()
        
        # Determine Count_Min
        # Count all aces in the hand has "low", that is, having 1 pip.
        info.Count_Min = self.count_hand()
        
        # Determine Count_Max
        # Count aces in the hand. The first ace if any will be counted as "high" (i.e. 11), while any remaining will be counted as "low" (i.e. 1)
        # This is based on the logic that two (or more) aces all counted "high" will allways bust the hand.
        count_aces = 0
        if num_aces > 0:
            # There is at least one ace. Add one ace counted "high" (i.e. 11) to the count value of aces in the hand
            count_aces += self.get_aces().get_cards()[0].count_card(ace_high=True)
        if (num_aces - 1) > 0:
            # There is more than one ace. Add a "low" (i.e. 1) ace value to the count value of aces in the hand for each ace beyond one
            count_aces += (num_aces - 1) * self.get_aces().get_cards()[0].count_card(ace_high=False)
        info.Count_Max = info.Count_Other + count_aces

        return info
    

    def count_hand(self):
        """
        Count the hand, with any aces treated as "low".
        :return: The integer count value of the cards in the hand.
        """
        count = 0
        
        # TODO: Could use a lamda function maybe to compact this?
        for x in self._cards:
            count += x.count_card(ace_high=False)
                
        return count
    

    def remove_card(self, index = -1):
        """
        Remove the card at index from the hand. By default (index = -1), the last card will be removed.
        :parameter index: index of card to remove from the hand (starting at 0), int
        :return: The card that was removed from the had, Card
        """
        return self._cards.pop(index)
    
    
    def __str__(self):
        s = ''
        for x in self._cards:
            s += str(x) + ' '
        # Remove unneeded trailing space
        s = s[0:len(s)-1]
        return s       

        