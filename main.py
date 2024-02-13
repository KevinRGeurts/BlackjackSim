from deck import Stacked_Deck
from card import Card
from hand import Hand
from BlackJackSim import BlackJackSim, GamePlayOutcome, BlackJackGameOutcome
from PlayStrategy import InteractivePlayerPlayStrategy, InteractiveProbabilityPlayerPlayStrategy, ProbabilityPlayerPlayStrategy
from UserResponseCollector import UserResponseCollector_query_user, BlackJackQueryType
import logging
from pathlib import Path


def play_debug():
    """
    Run a debugging scenario coded in this function.
    """
    sim = BlackJackSim()
    
    dealer_hand = Hand()
    dealer_hand.add_cards([Card('D','J'),Card('H','K')])
    
    player_hand = Hand()
    player_hand.add_cards([Card('S','5'),Card('C','2')])
    
    (hit_win_prob, stand_win_prob, hit_push_prob, stand_push_prob) = sim.win_probability_hit_stand(player_hand,dealer_hand,1000)

    print('Hit Win Probability: ', hit_win_prob)
    print('Hit Push Probability: ', hit_push_prob)
    print('Stand Win Probability: ', stand_win_prob)
    print('Stand Push Probability: ', stand_push_prob)
        
    return None


def play_interactive_probability():
    """
    Use BlackJackSim to play an interactive game, but provid hit/stand win/push probability info to user.
    """
    sim = BlackJackSim()
    sim.set_player_play_strategy(InteractiveProbabilityPlayerPlayStrategy())
    print('Starting an interactive game of black jack with probability information...')
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
        print('     Split Winner:', info.Split_Game_Outcome)
        print('     Split Status:', info.Split_Status)
        print('     Split Count:', info.Split_Count)
        print('     Split Hand:', info.Split_Final_Hand)

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
        print('     Split Winner:', info.Split_Game_Outcome)
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
    if info.Split_Game_Outcome != BlackJackGameOutcome.NONE:
        # A pair was split. Provide output for the second player hand
        print('     Split Winner:', info.Split_Game_Outcome)
        print('     Split Status:', info.Split_Status)
        print('     Split Count:', info.Split_Count)
        print('     Split Hand:', info.Split_Final_Hand)
        
    return None


def play_many_auto():
    """
    Use BlackJackSim to play a bunch of games automatically.
    Example: Use this to see how often the player wins if they are dealt JH 9S, and dealer shows 7D.
    """

    # Get the hit/stand data logger so we can add a file handler to it if needed below
    logger = logging.getLogger('blackjack_logger.hit_stand_logger')

    sim = BlackJackSim()
    print('Starting a bunch of games of black jack to generate win statistics...')
    
    # Ask if hit/stand data should be logged to file
    query_preface = 'Do you want to log hit/stand data to file?'
    query_dic = {'y':'Yes', 'n':'No'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    fh = None # Because we need to have this variable in the outer scope
    if response == 'y':
            # TODO: Investigate if the generalization below will work on LINUX
            # We will always use the same log file name, placed in the user's Documents directory.
            home_path = Path().home().joinpath('Documents','hit_stand_training_data.log')
            fh = sim.setup_hit_stand_logging_file_handler(str(home_path))    

    # Ask how many games the user wants to have played
    # Build a query to ask how many games the user wants to have played
    query_preface = 'How many games do you want to automatically play?'
    num_games = UserResponseCollector_query_user(BlackJackQueryType.NUMBER, query_preface)
    
    # Ask if the user wants to specify the player's deal?
    player_deal = []
    player_init_hand = ''
    # Build a query to ask if the user wants to specify the player's deal
    query_preface = 'Do you want to specify the player''s deal?'
    query_dic = {'y':'Yes', 'n':'No'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    if response == 'y':
        # Build a query to get up to two cards from the user
        query_preface = 'Enter player deal of one or two cards.'
        player_deal = UserResponseCollector_query_user(BlackJackQueryType.CARDS, query_preface)
    
        # Rebuild what should be the input string of cards provided by the user.
        # This will be printed in the output as proof that the user input as produced the desired result.
        for i in range(len(player_deal)):
            player_init_hand += str(player_deal[i]) + ' '
    
    # Ask if the user wants to specify the dealer's show card?    
    dealer_show = None
    # Build a query to ask if the user wants to specify the dealer's show card
    query_preface = 'Do you want to specify the dealer''s show card?'
    query_dic = {'y':'Yes', 'n':'No'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    if response == 'y':
        # Build a query to get one card from the user
        query_preface = 'Enter one dealer show card.'
        dealer_show = UserResponseCollector_query_user(BlackJackQueryType.CARDS, query_preface)[0]

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
    
    
    # Remove the file handler from the logger, if file handler was created.
    # This ensures that each time through this function in the same execution of __main__ that the user gets to
    # decide if logging to file should happen.
    if fh is not None:
        logger.removeHandler(fh)

    return None


def play_many_probabilities_auto():
    """
    Use BlackJackSim to play a bunch of games automatically.
    But using calculated probabilities of win/push to determine whether to hit or stand.
    Example: Use this to see how often the player wins if they are a savant and can compute probabilities in their head :)
    """

    # Get the hit/stand data logger so we can add a file handler to it if needed below
    logger = logging.getLogger('blackjack_logger.hit_stand_logger')

    sim = BlackJackSim()
    sim.set_player_play_strategy(ProbabilityPlayerPlayStrategy())
    print('Starting a bunch of games of black jack to generate win statistics, and using win/push probabilities to hit/stand...')
    
    # Ask if hit/stand data should be logged to file
    query_preface = 'Do you want to log hit/stand data to file?'
    query_dic = {'y':'Yes', 'n':'No'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    fh = None # Because we need to have this variable in the outer scope
    if response == 'y':
            # TODO: Investigate if the generalization below will work on LINUX
            # We will always use the same log file name, placed in the user's Documents directory.
            home_path = Path().home().joinpath('Documents','hit_stand_training_data.log')
            fh = sim.setup_hit_stand_logging_file_handler(str(home_path))    

    # Ask how many games the user wants to have played
    # Build a query to ask how many games the user wants to have played
    query_preface = 'How many games do you want to automatically play?'
    num_games = UserResponseCollector_query_user(BlackJackQueryType.NUMBER, query_preface)
    
    # Ask if the user wants to specify the player's deal?
    player_deal = []
    player_init_hand = ''
    # Build a query to ask if the user wants to specify the player's deal
    query_preface = 'Do you want to specify the player''s deal?'
    query_dic = {'y':'Yes', 'n':'No'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    if response == 'y':
        # Build a query to get up to two cards from the user
        query_preface = 'Enter player deal of one or two cards.'
        player_deal = UserResponseCollector_query_user(BlackJackQueryType.CARDS, query_preface)
    
        # Rebuild what should be the input string of cards provided by the user.
        # This will be printed in the output as proof that the user input as produced the desired result.
        for i in range(len(player_deal)):
            player_init_hand += str(player_deal[i]) + ' '
    
    # Ask if the user wants to specify the dealer's show card?    
    dealer_show = None
    # Build a query to ask if the user wants to specify the dealer's show card
    query_preface = 'Do you want to specify the dealer''s show card?'
    query_dic = {'y':'Yes', 'n':'No'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    if response == 'y':
        # Build a query to get one card from the user
        query_preface = 'Enter one dealer show card.'
        dealer_show = UserResponseCollector_query_user(BlackJackQueryType.CARDS, query_preface)[0]

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
    
    
    # Remove the file handler from the logger, if file handler was created.
    # This ensures that each time through this function in the same execution of __main__ that the user gets to
    # decide if logging to file should happen.
    if fh is not None:
        logger.removeHandler(fh)

    return None    


def play_batches():
    """
    Use BlackJackSim to play a bunch of batches of games automatically.
    Example: Use this to see the distibution of net wins if you play 20 hands of blackjack many times.
    """
    sim = BlackJackSim()
    print('Playing batches of blackjack games to determine distribution of net wins for a batch...')
    
    # Ask how many games the user wants to have played in each batch
    # Build a query to ask how many games the user wants to have played in each batch
    query_preface = 'How many games per batch do you want to automatically play?'
    num_games = UserResponseCollector_query_user(BlackJackQueryType.NUMBER, query_preface)
    
    # Ask how many batches the user wants to have played
    # Build a query to ask how many batches the user wants to have played
    query_preface = 'How many batches do you want to automatically play?'
    num_batches = UserResponseCollector_query_user(BlackJackQueryType.NUMBER, query_preface)
    
    # If you need repeatability, for example to debug something, then you can set a seed here.
    from random import seed
    seed(1234567890)

    results = sim.play_batches_of_games(num_games, num_batches)

    for k, v in results.items():
        print('net wins: ', k, 'number of times:', v)

    return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    """
    Query the user for how they wish to use the BlackJack simulator, and then launch that usage.
    This includes a "debug" usage to set up what ever situation is needed for debugging, since I can't seem to reliably debug unit tests.
    """
    
    # Set up logging
    BlackJackSim().setup_logging()
    
    print('*** Python Blackjack Simulator ***')
    
    # Build a query for the user to obtain their choice of how to user the simulator
    query_preface = 'How do you want to use the simulator?'
    query_dic = {'q':'Quit', 'i':'Interactive Game', 'p':'Interactive Game with Probabilities', 'a':'Automatic Game', 'm':'Many Automatic Games', 'u':'Many Automatic Games Using Probabilities'   , 'b':'Batches of Games', 'd':'Debug Scenario'}
    response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
    
    while response != 'q':
        
        match response:
            
            case 'i':
                play_interactive()
                
            case 'a':
                play_one_auto()
                
            case 'm':
                play_many_auto()
                
            case 'b':
                play_batches()
                
            case 'p':
                play_interactive_probability()
                
            case 'u':
                play_many_probabilities_auto()
                
            case 'd':
                play_debug()
                
        response = UserResponseCollector_query_user(BlackJackQueryType.MENU, query_preface, query_dic)
      
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


