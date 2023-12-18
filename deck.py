from card import Card
from random import randrange

class Deck:
    """
    Represents a deck of playing cards.\n
    """
    
    def __init__(self, isInfinite = False):
        """
        Construct a deck from a list of Card's.
        If isInfinite, then when drawing cards from the deck, the deck will not be used up.
        """
        self.isInfinite = isInfinite
        # Build a standard deck of 52 playing cards as a list
        self.deck=[]
        self.deck.append(Card('S','A',1))
        self.deck.append(Card('S','2',2))
        self.deck.append(Card('S','3',3))
        self.deck.append(Card('S','4',4))
        self.deck.append(Card('S','5',5))
        self.deck.append(Card('S','6',6))
        self.deck.append(Card('S','7',7))
        self.deck.append(Card('S','8',8))
        self.deck.append(Card('S','9',9))
        self.deck.append(Card('S','10',10))
        self.deck.append(Card('S','J',10))
        self.deck.append(Card('S','Q',10))
        self.deck.append(Card('S','K',10))
        self.deck.append(Card('C','A',1))
        self.deck.append(Card('C','2',2))
        self.deck.append(Card('C','3',3))
        self.deck.append(Card('C','4',4))
        self.deck.append(Card('C','5',5))
        self.deck.append(Card('C','6',6))
        self.deck.append(Card('C','7',7))
        self.deck.append(Card('C','8',8))
        self.deck.append(Card('C','9',9))
        self.deck.append(Card('C','10',10))
        self.deck.append(Card('C','J',10))
        self.deck.append(Card('C','Q',10))
        self.deck.append(Card('C','K',10))       
        self.deck.append(Card('H','A',1))
        self.deck.append(Card('H','2',2))
        self.deck.append(Card('H','3',3))
        self.deck.append(Card('H','4',4))
        self.deck.append(Card('H','5',5))
        self.deck.append(Card('H','6',6))
        self.deck.append(Card('H','7',7))
        self.deck.append(Card('H','8',8))
        self.deck.append(Card('H','9',9))
        self.deck.append(Card('H','10',10))
        self.deck.append(Card('H','J',10))
        self.deck.append(Card('H','Q',10))
        self.deck.append(Card('H','K',10))
        self.deck.append(Card('D','A',1))
        self.deck.append(Card('D','2',2))
        self.deck.append(Card('D','3',3))
        self.deck.append(Card('D','4',4))
        self.deck.append(Card('D','5',5))
        self.deck.append(Card('D','6',6))
        self.deck.append(Card('D','7',7))
        self.deck.append(Card('D','8',8))
        self.deck.append(Card('D','9',9))
        self.deck.append(Card('D','10',10))
        self.deck.append(Card('D','J',10))
        self.deck.append(Card('D','Q',10))
        self.deck.append(Card('D','K',10))


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
        
            
            
            
            
        