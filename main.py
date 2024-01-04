from deck import Deck, Stacked_Deck
from hand import Hand
from card import Card
from BlackJackSim import BlackJackSim

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    """
    Used currently to set up what ever situation is needed for debugging, since I can't seem to debug unit tests.
    """
    
    # Debug creating a drawing from a Stacked_Deck
    sd = Stacked_Deck()
    sd.deck = [Card('S','J',10), Card('H','3',3), Card('S','5',5), Card("D","A",1),  Card("C","A",1)]
    c = sd.draw()
    print('Stacked Deck Draw:', c.print_card())

    # Debug adding a single card to a hand
    h = Hand()
    c = Card('S','J',10)
    h.add_cards(c)   
    
    # Debug drawing from a dec of cards

    d = Deck()
    c = d.draw()
    
    # Debug printing a hand to a string
    
    h = Hand()
    cards=[Card('S','J',10), Card('H','3',3), Card('S','5',5), Card("D","A",1),  Card("C","A",1)]
    h.add_cards(cards)
        
    act_val = h.print_hand()
    
    print(act_val + '\n')
    
    # Use BlackJackSim to play a hand as a dealer
    sim = BlackJackSim()
    sim.play_game()
    
    
    # # Work out the logic for playing a hand as a dealer
    
    # print('Starting dealer hand play...')
    
    # d = Deck(isInfinite = True)
    # h = Hand()
    # h.add_cards(d.draw(2))
    # print('Initial Dealer Hand: ' + h.print_hand())
    # info = h.hand_info()
    # print(info)
    
    # hand_status = ''
    # final_count = 0
    # # Hit as many times as needed until Count_Max exceeds 16
    # while info['Count_Max'] <= 16:
    #     # Hit
    #     hand_status = 'hit'
    #     h.add_cards(d.draw(1))
    #     print('Dealer Hand After Hitting on Max Count: ' + h.print_hand())
    #     info = h.hand_info()
    #     print(info) 
    # count_max = info['Count_Max']
    # if (count_max >= 17) and (count_max <= 21):
    #     # Stand on Count_Max
    #     hand_status = 'stand'
    #     final_count = count_max
    # elif count_max > 21:
    #     # If we've busted on Count_Max, switch to Count_Min
    #     while info['Count_Min'] <= 16:
    #         # Hit
    #         hand_status = 'hit'
    #         h.add_cards(d.draw(1))
    #         print('Dealer Hand After Hiting on Count_Min: ' + h.print_hand())
    #         info = h.hand_info()
    #         print(info)
    #     count_min = info['Count_Min']
    #     if (count_min >= 17) and (count_min <= 21):
    #         # Stand on Count_Min
    #         hand_status = 'stand'
    #         final_count = count_min
    #     elif count_min > 21:
    #         # If we've busted on Count_Min, and the hand
    #         hand_status = 'bust'
    #         final_count = count_min
    # print('Dealer Hand Outcome:', hand_status, final_count)


    # count = info['Count_Other'] + info['Num_Aces'] * 11
    # while count <= 16:
    #     h.add_cards(d.draw(1))
    #     print('Dealer Hand After Draw: ' + h.print_hand())
    #     info = h.hand_info()
    #     print(info)
    #     count = info['Count_Other'] + info['Num_Aces'] * 11
    # if count > 21:
    #     print('Dealer Busts')
    
    #if count > 21 and info['Num_Aces'] == 1:
    #   count = info['Count_Other'] + info['Num_Aces'] * 1
        
        
        
    
