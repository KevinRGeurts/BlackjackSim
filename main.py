from deck import Deck, Stacked_Deck
from hand import Hand
from card import Card
from BlackJackSim import BlackJackSim
from PlayStrategy import CasinoDealerPlayStrategy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    """
    Used currently to set up what ever situation is needed for debugging, since I can't seem to debug unit tests.
    """
    
    # # *** Debug creating a drawing from a Stacked_Deck ***
    # sd = Stacked_Deck()
    # sd.deck = [Card('S','J',10), Card('H','3',3), Card('S','5',5), Card("D","A",1),  Card("C","A",1)]
    # c = sd.draw()
    # print('Stacked Deck Draw:', c.print_card())

    # # *** Debug adding a single card to a hand ***
    # h = Hand()
    # c = Card('S','J',10)
    # h.add_cards(c)   
    
    # # *** Debug drawing from a dec of cards ***

    # d = Deck()
    # c = d.draw()
    
    # # *** Debug printing a hand to a string ***
    
    # h = Hand()
    # cards=[Card('S','J',10), Card('H','3',3), Card('S','5',5), Card("D","A",1),  Card("C","A",1)]
    # h.add_cards(cards)
        
    # act_val = h.print_hand()
    
    # print(act_val + '\n')
    
    
    # *** Use BlackJackSim to play a game ***

    # Dealer_Final_Hand = String representation of dealer's hand of cards at the end of the game, string
    # Dealer_Status = 'bust', 'stand', or 'blackjack', string
    # Dealer_Count = Final count of dealer's hand, int
    # Player_Final_Hand = String representation of Player's hand of cards at the end of the game, string
    # Player_Status = 'bust', 'stand', or 'blackjack', string
    # Player_Count = Final count of Player's hand, int
    # Game_Outcome = 'player wins', 'dealer wins', or 'push' (both blackjack, bust, or stand with a tie count)

    sim = BlackJackSim()
    print('Starting a game of black jack...')
    info = sim.play_game()
    print('     Winner:', info['Game_Outcome'])
    print('     Player Status:', info['Player_Status'])
    print('     Player Count:', info['Player_Count'])
    print('     Player Hand:', info['Player_Final_Hand'])
    print('     Dealer Status:', info['Dealer_Status'])
    print('     Dealer Count:', info['Dealer_Count'])
    print('     Dealer Hand:', info['Dealer_Final_Hand'])
    
    # # *** Use BlackJackSim to play a game with a stacked deck to produce a desired outcome ***

    # bjs = BlackJackSim()
    # print('Starting a game of black jack with a stacked deck to have player and dealer get blackjack...')
        
    # # Replace sim's deck with Stacked_Deck
    # # Create a Stacked_Deck
    # sd = Stacked_Deck()
    # # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
    # sd.deck = [Card('C','A',1), Card('D','K',10), Card('S','10',10), Card('H','A',1)]
    # # Replace sim's deck with the Stacked_Deck
    # bjs.deck = sd
       
    # info = bjs.play_game()
    # print('     Winner:', info['Game_Outcome'])
    # print('     Player Status:', info['Player_Status'])
    # print('     Player Count:', info['Player_Count'])
    # print('     Player Hand:', info['Player_Final_Hand'])
    # print('     Dealer Status:', info['Dealer_Status'])
    # print('     Dealer Count:', info['Dealer_Count'])
    # print('     Dealer Hand:', info['Dealer_Final_Hand'])
  
    
    # # Use BlackJackSim to play a hand as a dealer
    # sim = BlackJackSim()
    # sim.play_game()
    
    
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

    # # *** Debug playing srategy ***
    
    # ps = CasinoDealerPlayStrategy()
    # info = {}      
       
    # # Create a Stacked_Deck
    # sd = Stacked_Deck()
    # sd.deck = [Card('C','A',1), Card('D','3',3)]
       
    # # Set up hand
    # h = Hand()
    # h.add_cards([Card('S','7',7), Card('H','8',8)])
        
    # # Play the hand
    # info = ps.play(h, sd)

        
        
        
    
