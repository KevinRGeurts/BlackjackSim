from deck import Stacked_Deck
from card import Card
from BlackJackSim import BlackJackSim, GamePlayOutcome, BlackJackGameOutcome
from PlayStrategy import InteractivePlayerPlayStrategy


# TODO: Find a better home for this capability. As part of Card()? As part of Hand()?
def make_card_list_from_str(card_str = ''):
    """
    Make and return a list of cards, given a string in the format of Hand.__str__().
    :parameter card_str: A sting representing one or more cards in the format PipsSuit, e.g. AS KH QD JC 10H 2S
    :return: A list of Card()s
    """
    cards = []
    # Convert the card_str into a list of strings for individual cards, using str.split()
    card_str_list = card_str.split()
    for s in card_str_list:
        # Last character for each card string is the suit
        suit = s[len(s)-1]
        # The rest of the card string is the pips
        pips = s[0:len(s)-1]
        # Construct a Card() and add it to the return list
        # print('suit=',suit,'pips=',pips)
        cards.append(Card(suit, pips))   
    return cards


def play_debug():
    """
    Run a debugging scenario coded in this function.
    """
    sim = BlackJackSim()
        
    info = GamePlayOutcome()

    # Here is what will happen to the cards in the stacked deck
    # 1,2 dealt to dealer
    # 3,4 dealt to player before split
    # 5 dealt to player's split hand
    # 6 dealt to player's original hand after split
    sd = Stacked_Deck()
    sd.add_cards([Card('H','7'), Card('D','10'),Card('C','8'), Card('S','8'),Card('S','A'), Card('C','J')])
    sim.switch_deck(sd)
        
    # Play the game, which should result in a split
    info = sim.play_game()

    return None


def play_interactive():
    """
    Use BlackJackSim to play an interactive game.
    """
    sim = BlackJackSim()
    sim.set_player_play_strategy(InteractivePlayerPlayStrategy())
    print('Starting an interactive game of black jack...')
    info = sim.play_game()
    print('     Winner:', info.Game_Outcome)
    print('     Player Status:', info.Player_Status)
    print('     Player Count:', info.Player_Count)
    print('     Player Hand:', info.Player_Final_Hand)
    print('     Dealer Status:', info.Dealer_Status)
    print('     Dealer Count:', info.Dealer_Count)
    print('     Dealer Hand:', info.Dealer_Final_Hand)
    if info.Split_Game_Outcome != BlackJackGameOutcome.NONE:
        # A pair was split. Provide output for the second player hand
        print('     Winner:', info.Split_Game_Outcome)
        print('     Split Status:', info.Split_Status)
        print('     Split Count:', info.Split_Count)
        print('     Split Hand:', info.Split_Final_Hand)

    return None


def play_one_auto():
    """
    Use BlackJackSim to play one game automatically.
    """
    sim = BlackJackSim()
    print('Starting a game of black jack...')
    info = sim.play_game()
    print('     Winner:', info.Game_Outcome)
    print('     Player Status:', info.Player_Status)
    print('     Player Count:', info.Player_Count)
    print('     Player Hand:', info.Player_Final_Hand)
    print('     Dealer Status:', info.Dealer_Status)
    print('     Dealer Count:', info.Dealer_Count)
    print('     Dealer Hand:', info.Dealer_Final_Hand)
    if info.Split_Game_Out != BlackJackGameOutcome.NONE:
        # A pair was split. Provide output for the second player hand
        print('     Winner:', info.Split_Game_Outcome)
        print('     Split Status:', info.Split_Status)
        print('     Split Count:', info.Split_Count)
        print('     Split Hand:', info.Split_Final_Hand)
        
    return None


def play_many_auto():
    """
    Use BlackJackSim to play a bunch of games automatically.
    Example: Use this to see how often the player wins if they are dealt JH 9S, and dealer shows 7D.
    """
    sim = BlackJackSim()
    print('Starting a bunch of games of black jack to generate win statistics...')
    
    # Ask how many games the user wants to have played
    response = input('How many games do you want to automatically play?\n')
    num_games = int(response)
    
    # Ask if the user wants to specify the player's deal?
    player_deal = []
    player_init_hand = ''
    response = input('Do you want to specify the player''s deal? (Y/N)\n')
    if response == 'Y' or response == 'y':
        response = input('Enter player deal, e.g., 10H 5S: ')
        player_deal = make_card_list_from_str(response)
    
        # Rebuild what should be the input string of cards provided by the user.
        # This will be printed in the output as proof that the user input as produced the desired result.
        for i in range(len(player_deal)):
            player_init_hand += str(player_deal[i]) + ' '
    
    # Ask if the user wants to specify the dealer's show card?    
    dealer_show = None
    response = input('Do you want to specify the dealer''s show card? (Y/N)\n')
    if response == 'Y' or response == 'y':
        response = input('Enter dealer show, e.g., 10H: ')
        dealer_show = make_card_list_from_str(response)[0]

    # If you need repeatability, for example to debug something, then you can set a seed here.
    # from random import seed
    # seed(1234567890)

    info = sim.play_games(num_games, player_deal, dealer_show)
    dw = info.Dealer_Wins
    pw = info.Player_Wins
    pu = info.Pushes
    tg = dw + pw + pu
    dbj = info.Dealer_BlackJacks
    pbj = info.Player_BlackJacks
    
    print('     Dealer shows:', str(dealer_show))
    print('     Player initial hand:', player_init_hand)
    print('     Dealer Wins:', dw)
    print('     Player Wins:', pw)
    print('     Pushes:', pu)
    print('     Games Played:', tg)
    print('     Dealer % Wins:', ((100.0 * dw) / tg))
    print('     Player % Wins:', ((100.0 * pw) / tg))
    print('     Push %:', ((100.0 * pu) / tg))
    print('     Dealer BlackJacks:', dbj)
    print('     Player BlackJacks:', pbj)
    print('     Dealer % BlackJacks:', ((100.0 * dbj) / tg))
    print('     Player % BlackJacks:', ((100.0 * pbj) / tg))
    
    
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    """
    Used currently to set up what ever situation is needed for playing or debugging, since I can't seem to debug unit tests.
    """
    
    print('***Python Blackjack Simulator ***')
    
    # Ask user how they want to use the simulator
    response = input('(Q)uit, (I)nteractive Game, (A)utomatic Game, (M)any Automatic Games, (D)ebug Scenario ?\n')
    
    while response != 'Q' and response != 'q':
        
        match response:
            
            case 'I' | 'i':
                play_interactive()
                
            case 'A' | 'a':
                play_one_auto()
                
            case 'M' | 'm':
                play_many_auto()
                
            case 'D' | 'd':
                play_debug()
                
        response = input('(Q)uit, (I)nteractive Game, (A)utomatic Game, (M)any Automatic Games')
    
      
    # *** Use BlackJackSim to play a game with a stacked deck to produce a desired outcome ***

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
    # print('     Winner:', info.Game_Outcome)
    # print('     Player Status:', info.Player_Status)
    # print('     Player Count:', info.Player_Count)
    # print('     Player Hand:', info.Player_Final_Hand)
    # print('     Dealer Status:', info.Dealer_Status)
    # print('     Dealer Count:', info.Dealer_Count)
    # print('     Dealer Hand:', info.Dealer_Final_Hand)
    # if info.Split_Game_Out != BlackJackGameOutcome.NONE:
    #     # A pair was split. Provide output for the second player hand
    #     print('     Winner:', info.Split_Game_Outcome)
    #     print('     Split Status:', info.Split_Status)
    #     print('     Split Count:', info.Split_Count)
    #     print('     Split Hand:', info.Split_Final_Hand)


