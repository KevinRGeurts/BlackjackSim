from deck import Deck, Stacked_Deck
from hand import Hand
from card import Card
from BlackJackSim import BlackJackSim
from PlayStrategy import CasinoDealerPlayStrategy, HoylePlayerPlayStrategy, InteractivePlayerPlayStrategy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    """
    Used currently to set up what ever situation is needed for playing or debugging, since I can't seem to debug unit tests.
    """
    
    # *** Use BlackJackSim to play an interactive game ***

    sim = BlackJackSim()
    sim.set_player_play_strategy(InteractivePlayerPlayStrategy())
    print('Starting an interactive game of black jack...')
    info = sim.play_game()
    print('     Winner:', info['Game_Outcome'])
    print('     Player Status:', info['Player_Status'])
    print('     Player Count:', info['Player_Count'])
    print('     Player Hand:', info['Player_Final_Hand'])
    print('     Dealer Status:', info['Dealer_Status'])
    print('     Dealer Count:', info['Dealer_Count'])
    print('     Dealer Hand:', info['Dealer_Final_Hand'])    
    
    
    # *** Use BlackJackSim to play a game ***

    # Dealer_Final_Hand = String representation of dealer's hand of cards at the end of the game, string
    # Dealer_Status = 'bust', 'stand', or 'blackjack', string
    # Dealer_Count = Final count of dealer's hand, int
    # Player_Final_Hand = String representation of Player's hand of cards at the end of the game, string
    # Player_Status = 'bust', 'stand', or 'blackjack', string
    # Player_Count = Final count of Player's hand, int
    # Game_Outcome = 'player wins', 'dealer wins', or 'push' (both blackjack, bust, or stand with a tie count)

    # sim = BlackJackSim()
    # print('Starting a game of black jack...')
    # info = sim.play_game()
    # print('     Winner:', info['Game_Outcome'])
    # print('     Player Status:', info['Player_Status'])
    # print('     Player Count:', info['Player_Count'])
    # print('     Player Hand:', info['Player_Final_Hand'])
    # print('     Dealer Status:', info['Dealer_Status'])
    # print('     Dealer Count:', info['Dealer_Count'])
    # print('     Dealer Hand:', info['Dealer_Final_Hand'])
    
    
    # *** Use BlackJackSim to play a bunch of games ***

    # Dealer_Wins = The number of games won by the dealer, int
    # Player_WIns = The number of games won by the player, int
    # Pushes = The number of tie (push) games, int
    
    # sim = BlackJackSim()
    # player_deal=[Card('H','J'), Card('S','9')]
    # player_init_hand = ''
    # for i in range(len(player_deal)):
    #     player_init_hand += str(player_deal[i]) + ' '
    # dealer_show=Card('D','7')
    # print('Starting a bunch of games of black jack to generate win statistics...')
    # print('Using a starting hand for player and a starting show card for dealer...')
    
    # #from random import seed
    # #seed(1234567890)
    # info = sim.play_games(100, player_deal, dealer_show)
    # dw = info['Dealer_Wins']
    # pw = info['Player_Wins']
    # pu = info['Pushes']
    # tg = dw + pw + pu
    # print('     Dealer shows:', str(dealer_show))
    # print('     Player initial hand:', player_init_hand)
    # print('     Dealer Wins:', dw)
    # print('     Player Wins:', pw)
    # print('     Pushes:', pu)
    # print('     Games Played:', tg)
    # print('     Dealer % Wins:', ((100.0 * dw) / tg))
    # print('     Player % Wins:', ((100.0 * pw) / tg))
    # print('     Push %:', ((100.0 * pu) / tg))
    
    
    # # *** Use BlackJackSim to play a game with a stacked deck to produce a desired outcome ***

    # bjs = BlackJackSim()
    # print('Starting a game of black jack with a stacked deck to have player and dealer get blackjack...')
        
    # # Replace sim's deck with Stacked_Deck
    # # Create a Stacked_Deck
    # sd = Stacked_Deck()
    # # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
    # sd.add_cards([Card('C','A'), Card('D','K'), Card('S','10'), Card('H','A')])
    # # Replace sim's deck with the Stacked_Deck
    # bjs.switch_deck(sd)
       
    # info = bjs.play_game()
    # print('     Winner:', info['Game_Outcome'])
    # print('     Player Status:', info['Player_Status'])
    # print('     Player Count:', info['Player_Count'])
    # print('     Player Hand:', info['Player_Final_Hand'])
    # print('     Dealer Status:', info['Dealer_Status'])
    # print('     Dealer Count:', info['Dealer_Count'])
    # print('     Dealer Hand:', info['Dealer_Final_Hand'])
