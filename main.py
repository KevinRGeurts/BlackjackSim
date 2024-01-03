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
    
    print(act_val + '\n')
    
    # Work out the logic for playing a hand as a dealer
    
    d = Deck(isInfinite = True)
    h = Hand()
    h.add_cards(d.draw(2))
    print('Initial Dealer Hand: ' + h.print_hand())
    info = h.hand_info()
    print(info)
    
    count = info['Count_Other'] + info['Num_Aces'] * 11
    while count <= 16:
        h.add_cards(d.draw(1))
        print('Dealer Hand After Draw: ' + h.print_hand())
        info = h.hand_info()
        print(info)
        count = info['Count_Other'] + info['Num_Aces'] * 11
    if count > 21:
        print('Dealer Busts')
    
    #if count > 21 and info['Num_Aces'] == 1:
    #   count = info['Count_Other'] + info['Num_Aces'] * 1
        
        
        
    
