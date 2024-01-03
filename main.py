from deck import Deck
from hand import Hand
from card import Card

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    """
    Used currently to set up what ever situation is needed for debugging, since I can't seem to debug unit tests.
    """
    
    # Debug drawing from a dec of cards

    d = Deck()
    c = d.draw()
    
    # Debug printing a hand to a string
    
    h = Hand()
    cards=[Card('S','J',10), Card('H','3',3), Card('S','5',5), Card("D","A",1),  Card("C","A",1)]
    h.add_cards(cards)
        
    act_val = h.print_hand()
    
    print(act_val)
    
