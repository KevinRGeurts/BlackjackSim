from asyncio.windows_events import NULL
from deck import Deck
from hand import Hand
from PlayStrategy import PlayStrategy, CasinoDealerPlayStrategy, HoylePlayerPlayStrategy

class BlackJackSim:
    """
    Logic for playing a game of black jack.\n
    """

    def __init__(self):
        """
        Construct an infinite deck of Cards (i.e. an infinite deck shute), an empty dealer Hand, and an empty player Hand.
        """
        self.deck = Deck(isInfinite = True)
        self.dealer_hand = Hand()
        #self.dealer_play_strategy = PlayStrategy()
        self.dealer_play_strategy = CasinoDealerPlayStrategy()
        self.player_hand = Hand()
        #self.player_play_strategy = PlayStrategy()
        self.player_play_strategy = HoylePlayerPlayStrategy()
        #self.player_play_strategy = CasinoDealerPlayStrategy()
        
    # TODO: Add ability to log detailed results of all individual games in a set to a text file for later analyis.
    # TODO: Add a type of game play where the player and/or dealer hand has some consistent initial partial or full deal before play begins. (To simulate specific situations sitting at the table where the player can't see the dealer's second card and is curious about the odds.)    

    
    def draw_for_dealer(self, number=1):
        """
        Draw one or more cards from deck into dealer's hand.
        :parameter number: How many cards to draw into dealer's hand, int
        :return: A list of Card(s) in the hand after the draw
        """
        return self.dealer_hand.add_cards(self.deck.draws(number))
    
        
    def draw_for_player(self, number=1):
        """
        Draw one or more cards from deck into player's hand.
        :parameter number: How many cards to draw into player's hand, int
        :return: A list of Card(s) in the hand after the draw
        """
        self.player_hand.add_cards(self.deck.draws(number))   
    
    
    def play_games(self, num_games = 1, player_deal = [], dealer_show = None):
        """
        Play multiple games of blackjack, returning a dictionary of statistics of outcomes across the set of games.
            Dealer_Wins = The number of games won by the dealer, int
            Player_WIns = The number of games won by the player, int
            Pushes = The number of tie (push) games, int
        :parameter num_games: The number of games to play, int
        :parameter player_deal: A list of no, one, or two Card()s dealt to the player. The deal will be completed with 2, 1, or no
            cards. This is intended to enable fixing part or all of the initial player hand.
        :paremeter dealer_show: If specified, it is the showing, face up Card() for the dealer, and one additional card will be
            drawn to complete the dealer's initial hand. This is intended to enable fixing the part of the dealer's hand which
            is visible to the player.
        :return: Dictionary of statistics for the set of games.
        """
        game_stats = {}
        
        dealer_wins = 0
        player_wins = 0
        pushes = 0
        
        for g in range(num_games):  
            print('Playing game:', g)
            info = self.play_game(player_deal, dealer_show)
            if info['Game_Outcome'] == 'dealer wins':
                dealer_wins += 1
            elif info['Game_Outcome'] == 'player wins':
                player_wins += 1
            elif info['Game_Outcome'] == 'push':
                pushes += 1
        
        game_stats['Dealer_Wins'] = dealer_wins
        game_stats['Player_Wins'] = player_wins
        game_stats['Pushes'] = pushes
               
        return game_stats

    
    def play_game(self, player_deal = [], dealer_show = None):
        """
        Play one game of black jack, returning a dictionary of information about the outcome of the game.
            Dealer_Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Dealer_Status = 'bust', 'stand', 'blackjack', or 'none' (player blackjacked, dealer didn't), string
            Dealer_Count = Final count of dealer's hand (0 if player blackjacked and dealer didn't), int
            Player_Final_Hand = String representation of Player's hand of cards at the end of the game, string
            Player_Status = 'bust', 'stand', 'blackjack', or 'none'  (dealer blackjacked, player didn't), string
            Player_Count = Final count of Player's hand (0 if dealer blackjacked and player didn't), int
            Game_Outcome = 'player wins', 'dealer wins', or 'push' (both blackjack, bust, or stand with a tie count)
        :parameter player_deal: A list of no, one, or two Card()s dealt to the player. The deal will be completed with 2, 1, or no
            cards. This is intended to enable fixing part or all of the initial player hand.
        :paremeter dealer_show: If specified, it is the showing, face up Card() for the dealer, and one additional card will be
            drawn to complete the dealer's initial hand. This is intended to enable fixing the part of the dealer's hand which
            is visible to the player.
        :return: Dictionary of information about the outcome of the game.
        """
        info = {}
        
        # Clear dealer and player hands of Cards
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        
        # Build the dealer's initial hand, drawing as needed
        if dealer_show is None:
            self.dealer_hand.add_cards(self.deck.draw(2))
        else:
            self.dealer_hand.add_cards(dealer_show)
            self.dealer_hand.add_cards(self.deck.draw(1))
            
        # Build the player's inital hand, drawing as needed
        assert(len(player_deal) <=2)
        self.player_hand.add_cards(player_deal)
        if len(player_deal) == 0:
            self.player_hand.add_cards(self.deck.draw(2))
        elif len(player_deal) == 1:
            self.player_hand.add_cards(self.deck.draw(1))
        
        # TODO: Should I handle splitting hands when the player gets a pair on the deal?
        
        check_info = self.check_for_blackjack()
        if check_info['Status'] == 'play on':
        
            # Neither dealer nor player have blackjack, on deal, so play the hands.
            
            # Play player hand, and add hand outcome info to game info
            player_info = {}
            player_info = self.play_player_hand()
            info['Player_Final_Hand'] = player_info['Final_Hand']
            info['Player_Status'] = player_info['Status']
            info['Player_Count'] = player_info['Count']       
        
            # Play dealer hand, and add hand outcome info to game info
            dealer_info = {}
            dealer_info = self.play_dealer_hand()
            info['Dealer_Final_Hand'] = dealer_info['Final_Hand']
            info['Dealer_Status'] = dealer_info['Status']
            info['Dealer_Count'] = dealer_info['Count']
                    
            # Determine game outcome, and add to game info
 
            self.determine_game_outcome(info)
         
        else:
            
            # One or both of dealer or/and player have blackjack. Set game outcome, etc. in game info

            info['Player_Final_Hand'] = str(self.player_hand)
            info['Dealer_Final_Hand'] = str(self.dealer_hand)
            
            if check_info['Status'] == 'both blackjack':
                # It's a tie score, and a push
                info['Game_Outcome'] = 'push'
                info['Player_Status'] = 'blackjack'
                info['Player_Count'] = 21
                info['Dealer_Status'] = 'blackjack'
                info['Dealer_Count'] = 21
            elif check_info['Status'] == 'dealer blackjack':
                info['Game_Outcome'] = 'dealer wins'
                info['Player_Status'] = 'none'
                info['Player_Count'] = 0
                info['Dealer_Status'] = 'blackjack'
                info['Dealer_Count'] = 21
            elif check_info['Status'] == 'player blackjack':
                info['Game_Outcome'] = 'player wins'
                info['Player_Status'] = 'blackjack'
                info['Player_Count'] = 21
                info['Dealer_Status'] = 'none'
                info['Dealer_Count'] = 0

        return info
        
    
    def check_for_blackjack(self):
        """
        Check both the dealer's and player's hand for black jack, and declare a winner (one hand has blackjack) or a push (both hands have blackjack). 
        Play the dealer's hand of black jack, returning a dictionary of information about the outcome of the hand.
            Status = 'play on', 'dealer blackjack', 'player blackjack', 'both blackjack', string
        :return: Dictionary of information about the outcome of the blackjack check.
        """      
        check_info = {}
        
        dealer_info = self.dealer_hand.hand_info()
        player_info = self.player_hand.hand_info()
        
        if dealer_info['Count_Max'] == 21 and player_info['Count_Max'] == 21:
            check_info['Status'] = 'both blackjack'
        elif dealer_info['Count_Max'] == 21:
            check_info['Status'] = 'dealer blackjack'
        elif player_info['Count_Max'] == 21:
            check_info['Status'] = 'player blackjack'
        else:
            check_info['Status'] = 'play on'
            
        return check_info
    
    
    def play_dealer_hand(self):
        """
        Play the dealer's hand of black jack, using the dealer play strategy, and returning
        a dictionary of information about the outcome of the hand.
            Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Status = 'bust' or 'stand', string
            Count = Final count of dealer's hand, int
        :return: Dictionary of information about the outcome of the hand.
        """
        outcome_info = {}
        
        outcome_info = self.dealer_play_strategy.play(self.dealer_hand, self.deck)
                  
        return outcome_info
        
    def play_player_hand(self):
        """
        Play the player's hand of black jack, using the player play strategy, and returning
        a dictionary of information about the outcome of the hand.
            Final_Hand = String representation of player's hand of cards at the end of the game, string
            Status = 'bust' or 'stand', string
            Count = Final count of player's hand, int
        *** Play logic is currently the same as for dealer, which is not the ultimate goal, and is likely to end up with
        a poor outcome statistically for the player, since the player will tend to bust first due to order of play when using same logic. ***
        :return: Dictionary of information about the outcome of the hand.
        """
        outcome_info = {}
        
        # Get the first card in the dealer's hand, which is the face up card
        show = self.dealer_hand.get_cards()[0]
        
        outcome_info = self.player_play_strategy.play(self.player_hand, self.deck, show)
                    
        return outcome_info
    

    def determine_game_outcome(self, info = {}):
        """
        Complete the argument info dictionary after determing the game winner.
        Assumes that Player_Status, Dealer_Status, Player_Count, and Dealer_Count exist in the info dictionary upon entry to this method.
        :param info: same info object returned by play_game(), dictionary
        :return: NULL
        """
        if (info['Player_Status'] == 'bust'):
            # If player busts, then it doesn't matter what the dealer status is, the dealer wins.
            # This is the house's advantage in the game.
            info['Game_Outcome'] = 'dealer wins'
        elif (info['Player_Status'] == 'stand') and (info['Dealer_Status'] == 'bust'):
            info['Game_Outcome'] = 'player wins'
        else:
            # Both player and dealer stood, higher score wins
            if info['Player_Count'] > info['Dealer_Count']:
                # Player wins
                info['Game_Outcome'] = 'player wins'
            elif info['Player_Count'] < info['Dealer_Count']:
                # Dealer wins
                info['Game_Outcome'] = 'dealer wins'
            else:
                # It's a tie score, and a push
                info['Game_Outcome'] = 'push'
       
        return None;
    

