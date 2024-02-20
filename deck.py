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
        self._isInfinite = isInfinite
        self._deck = self.create_deck()


    def create_deck(self):
        """
        Create and return a list of cards that represents a regular decks of playing cards.
        :return: A list of Card()s, list
        """
        # Build a standard deck of 52 playing cards as a list
        deck = []
        deck.append(Card('S','A'))
        deck.append(Card('S','2'))
        deck.append(Card('S','3'))
        deck.append(Card('S','4'))
        deck.append(Card('S','5'))
        deck.append(Card('S','6'))
        deck.append(Card('S','7'))
        deck.append(Card('S','8'))
        deck.append(Card('S','9'))
        deck.append(Card('S','10'))
        deck.append(Card('S','J'))
        deck.append(Card('S','Q'))
        deck.append(Card('S','K'))
        deck.append(Card('C','A'))
        deck.append(Card('C','2'))
        deck.append(Card('C','3'))
        deck.append(Card('C','4'))
        deck.append(Card('C','5'))
        deck.append(Card('C','6'))
        deck.append(Card('C','7'))
        deck.append(Card('C','8'))
        deck.append(Card('C','9'))
        deck.append(Card('C','10'))
        deck.append(Card('C','J'))
        deck.append(Card('C','Q'))
        deck.append(Card('C','K'))       
        deck.append(Card('H','A'))
        deck.append(Card('H','2'))
        deck.append(Card('H','3'))
        deck.append(Card('H','4'))
        deck.append(Card('H','5'))
        deck.append(Card('H','6'))
        deck.append(Card('H','7'))
        deck.append(Card('H','8'))
        deck.append(Card('H','9'))
        deck.append(Card('H','10'))
        deck.append(Card('H','J'))
        deck.append(Card('H','Q'))
        deck.append(Card('H','K'))
        deck.append(Card('D','A'))
        deck.append(Card('D','2'))
        deck.append(Card('D','3'))
        deck.append(Card('D','4'))
        deck.append(Card('D','5'))
        deck.append(Card('D','6'))
        deck.append(Card('D','7'))
        deck.append(Card('D','8'))
        deck.append(Card('D','9'))
        deck.append(Card('D','10'))
        deck.append(Card('D','J'))
        deck.append(Card('D','Q'))
        deck.append(Card('D','K'))            
        return deck   


    def add_card(self, card = Card()):
        """
        Add the argument Card to the deck.
        :parameter card: The Card to add to the deck, Card
        :return: The current list of cards in the deck, a shallow copy of self._deck, list
        """
        self._deck.append(card)
        return list(self._deck)  # list(list) makes a shallow copy, which is what we want
    

    def add_cards(self, cards = []):
        """
        Add a list of Card()s to the deck.
        :paramter cards: Card()s to be added to the deck.
        :return: The current list of cards in the deck, a shallow copy of self._deck, list
        """
        for c in cards:
            self.add_card(c)
        return list(self._deck) # list(list) makes a shallow copy, which is what we want
            
    
    def cards_remaining(self):
        """
        Return the number of cards left in the deck.
        :return: The number of cards left in the deck.
        """
        return len(self._deck)
    
    
    def draw(self, number = 1):
        """
        Draw Card(s) at random from the deck. If deck _isInfinte = False, then the drawn Card(s) will be removed from deck.
        :param number: The number of c\Cards to draw from the deck
        :return: A single Card or a list of Card(s)
        """
        drawn=[]
        for c in range(number):
            if self.cards_remaining() < 1:
                # Deck is out of cards and needs to be restocked.
                self._deck = self.create_deck()
            i=randrange(self.cards_remaining())
            # Add random ith card to the list of drawn cards
            drawn.append(self._deck[i])
            if self._isInfinite == False:
                # Remove ith card from the deck
                del self._deck[i]
        if number == 1:
            return drawn[0]
        else:
            return drawn
        

    def __str__(self):
        s = ''
        for c in self._deck:
            s += (str(c) + ' ')
        return s[0:len(s)-1]
        

class ShoeDeck(Deck):
    """
    Represents a shoe of playing cards, from which cards can be drawn until the shoe is empty, and then it automatically
    refills itself.
    """
    
    def __init__(self, num_decks = 5):
        """
        Construct a shoe of num_decks regular decks of playing cards.
        :parameter num_decks: How many regular decks are their in the shoe?, int
        """
        self._isInfinite = False
        self._shoe_size = num_decks
        self._deck = self.create_shoe(self._shoe_size)
        
        
    def create_shoe(self, num_decks):
        """
        Create and return a list of cards that represents a shoe of num_decks regular decks of playing cards.
        :parameter num_decks: How many regular decks are their in the shoe?, int
        :return: A list of Card()s, list
        """
        shoe = []
        for d in range(num_decks):
            shoe.append(Card('S','A'))
            shoe.append(Card('S','2'))
            shoe.append(Card('S','3'))
            shoe.append(Card('S','4'))
            shoe.append(Card('S','5'))
            shoe.append(Card('S','6'))
            shoe.append(Card('S','7'))
            shoe.append(Card('S','8'))
            shoe.append(Card('S','9'))
            shoe.append(Card('S','10'))
            shoe.append(Card('S','J'))
            shoe.append(Card('S','Q'))
            shoe.append(Card('S','K'))
            shoe.append(Card('C','A'))
            shoe.append(Card('C','2'))
            shoe.append(Card('C','3'))
            shoe.append(Card('C','4'))
            shoe.append(Card('C','5'))
            shoe.append(Card('C','6'))
            shoe.append(Card('C','7'))
            shoe.append(Card('C','8'))
            shoe.append(Card('C','9'))
            shoe.append(Card('C','10'))
            shoe.append(Card('C','J'))
            shoe.append(Card('C','Q'))
            shoe.append(Card('C','K'))       
            shoe.append(Card('H','A'))
            shoe.append(Card('H','2'))
            shoe.append(Card('H','3'))
            shoe.append(Card('H','4'))
            shoe.append(Card('H','5'))
            shoe.append(Card('H','6'))
            shoe.append(Card('H','7'))
            shoe.append(Card('H','8'))
            shoe.append(Card('H','9'))
            shoe.append(Card('H','10'))
            shoe.append(Card('H','J'))
            shoe.append(Card('H','Q'))
            shoe.append(Card('H','K'))
            shoe.append(Card('D','A'))
            shoe.append(Card('D','2'))
            shoe.append(Card('D','3'))
            shoe.append(Card('D','4'))
            shoe.append(Card('D','5'))
            shoe.append(Card('D','6'))
            shoe.append(Card('D','7'))
            shoe.append(Card('D','8'))
            shoe.append(Card('D','9'))
            shoe.append(Card('D','10'))
            shoe.append(Card('D','J'))
            shoe.append(Card('D','Q'))
            shoe.append(Card('D','K'))            
        return shoe
    
    
    def draw(self, number = 1):
        """
        Draw Card(s) at random from the deck. If deck _isInfinte = False, then the drawn Card(s) will be removed from deck.
        :param number: The number of c\Cards to draw from the deck
        :return: A single Card or a list of Card(s)
        """
        drawn=[]
        for c in range(number):
            if self.cards_remaining() < 1:
                # Deck is out of cards and needs to be restocked.
                self._deck = self.create_shoe(self._shoe_size)
            i=randrange(self.cards_remaining())
            # Add random ith card to the list of drawn cards
            drawn.append(self._deck[i])
            if self._isInfinite == False:
                # Remove ith card from the deck
                del self._deck[i]
        if number == 1:
            return drawn[0]
        else:
            return drawn
 

class StackedDeck(Deck):
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
        self._isInfinite = False
        # Create an empty deck of playing cards as a list
        self._deck=[]
 
        
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
            drawn.append(self._deck[0])
            if self._isInfinite == False:
                # Remove 0th card from the deck
                del self._deck[0]
        if number == 1:
            return drawn[0]
        else:
            return drawn
 
        
            
            
            
            
        
