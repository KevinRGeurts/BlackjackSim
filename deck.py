from card import Card
from random import randrange

class Deck:
    """
    Represents a deck of playing cards.\n
    """
    
    def __init__(self, isInfinite = False):
        """
        Construct a deck as a list of Card's.
        If isInfinite, then when drawing cards from the deck, the deck will not be used up.
        """
        self.isInfinite = isInfinite
        # Build a standard deck of 52 playing cards as a list
        self.deck=[]
        self.deck.append(Card('S','A'))
        self.deck.append(Card('S','2'))
        self.deck.append(Card('S','3'))
        self.deck.append(Card('S','4'))
        self.deck.append(Card('S','5'))
        self.deck.append(Card('S','6'))
        self.deck.append(Card('S','7'))
        self.deck.append(Card('S','8'))
        self.deck.append(Card('S','9'))
        self.deck.append(Card('S','10'))
        self.deck.append(Card('S','J'))
        self.deck.append(Card('S','Q'))
        self.deck.append(Card('S','K'))
        self.deck.append(Card('C','A'))
        self.deck.append(Card('C','2'))
        self.deck.append(Card('C','3'))
        self.deck.append(Card('C','4'))
        self.deck.append(Card('C','5'))
        self.deck.append(Card('C','6'))
        self.deck.append(Card('C','7'))
        self.deck.append(Card('C','8'))
        self.deck.append(Card('C','9'))
        self.deck.append(Card('C','10'))
        self.deck.append(Card('C','J'))
        self.deck.append(Card('C','Q'))
        self.deck.append(Card('C','K'))       
        self.deck.append(Card('H','A'))
        self.deck.append(Card('H','2'))
        self.deck.append(Card('H','3'))
        self.deck.append(Card('H','4'))
        self.deck.append(Card('H','5'))
        self.deck.append(Card('H','6'))
        self.deck.append(Card('H','7'))
        self.deck.append(Card('H','8'))
        self.deck.append(Card('H','9'))
        self.deck.append(Card('H','10'))
        self.deck.append(Card('H','J'))
        self.deck.append(Card('H','Q'))
        self.deck.append(Card('H','K'))
        self.deck.append(Card('D','A'))
        self.deck.append(Card('D','2'))
        self.deck.append(Card('D','3'))
        self.deck.append(Card('D','4'))
        self.deck.append(Card('D','5'))
        self.deck.append(Card('D','6'))
        self.deck.append(Card('D','7'))
        self.deck.append(Card('D','8'))
        self.deck.append(Card('D','9'))
        self.deck.append(Card('D','10'))
        self.deck.append(Card('D','J'))
        self.deck.append(Card('D','Q'))
        self.deck.append(Card('D','K'))


    def cards_remaining(self):
        """
        Return the number of cards left in the deck.
        :return: The number of cards left in the deck.
        """
        return len(self.deck)
    
    
    def draw(self, number = 1):
        """
        Draw Card(s) at random from the deck. If deck isInfinte = False, then the drawn Card(s) will be removed from deck.
        :param number: The number of c\Cards to draw from the deck
        :return: A single Card or a list of Card(s)
        """
        drawn=[]
        for c in range(number):
            assert self.cards_remaining() >= 1
            i=randrange(self.cards_remaining())
            # Add random ith card to the list of drawn cards
            drawn.append(self.deck[i])
            if self.isInfinite == False:
                # Remove ith card from the deck
                del self.deck[i]
        if number == 1:
            return drawn[0]
        else:
            return drawn
        

    def __str__(self):
        s = ''
        for c in self.deck:
            s += (str(c) + ' ')
        return s[0:len(s)-1]
        

class Stacked_Deck(Deck):
    """
    Represents a stacked deck of playing cards. Where the deck can be ordered by the caller and cards will always be drawn top to bottom.
    Primary purpose of this special Deck is to facilitate unit testing of hand play.
    """
    
    def __init__(self):
        """
        Construct a deck as an empty list of Card's.
        Assumption here is that user will populate the list themselves, before calling any methods on an object.
        Otherwise, draw() will assert.
        Set isInfinite to False, so that when drawing cards from the deck, the deck will be used up.
        """
        self.isInfinite = False
        # Create an empty deck of playing cards as a list
        self.deck=[]
 
        
    def draw(self, number = 1):
        """
        Draw Card(s) in order from the deck, and remove them from the deck.
        :param number: The number of c\Cards to draw from the deck
        :return: A single Card or a list of Card(s)
        """
        drawn=[]
        for c in range(number):
            assert self.cards_remaining() >= 1
            # Add 0th card to the list of drawn cards
            drawn.append(self.deck[0])
            if self.isInfinite == False:
                # Remove 0th card from the deck
                del self.deck[0]
        if number == 1:
            return drawn[0]
        else:
            return drawn
 
        
            
            
            
            
        
