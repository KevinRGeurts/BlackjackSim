from asyncio.windows_events import NULL
from deck import Deck
from hand import Hand
from PlayStrategy import PlayStrategy, CasinoDealerPlayStrategy, HoylePlayerPlayStrategy, BlackJackPlayStatus
from enum import Enum


class BlackJackCheck(Enum):
    """
    An enumeration returned by BlackJackSim.chack_for_blackjack().
    """
    PLAY_ON = 1
    DEALER_BLACKJACK = 2
    PLAYER_BLACKJACK = 3
    BOTH_BLACKJACK = 4


class BlackJackGameOutcome(Enum):
    """
    An enumeration that is part of the object that represents the outcome of playing a game.
    """
    PLAYER_WINS = 1
    DEALER_WINS = 2
    # PUSH means both blackjack, bust, or stand with a tie count
    PUSH = 3


class GamePlayOutcome:
    """
    This class is a structured way of returning information about the outcome of playing a game of black jack, e.g., from play_game().
    Think of this as a C struct, where it is expected that data members will be direcly accessed, because this class has no methods, beyound __init__().
    """
    def __init__(self):
        """
        Create the data members of structured info.
            Dealer_Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Dealer_Status = 'bust', 'stand', 'blackjack', or 'none' (player blackjacked, dealer didn't), string
            Dealer_Count = Final count of dealer's hand (0 if player blackjacked and dealer didn't), int
            Player_Final_Hand = String representation of Player's hand of cards at the end of the game, string
            Player_Status = 'bust', 'stand', 'blackjack', or 'none'  (dealer blackjacked, player didn't), string
            Player_Count = Final count of Player's hand (0 if dealer blackjacked and player didn't), int
            Game_Outcome = Who won?, BlackJackGameOutcome() enum
        """
        self.Dealer_Final_Hand = ''
        self.Dealer_Status = BlackJackPlayStatus.STAND
        self.Dealer_Count = 0
        self.Player_Final_Hand = ''
        self.Player_Status = BlackJackPlayStatus.STAND
        self.Player_Count = 0
        self.Game_Outcome = BlackJackGameOutcome.PUSH
    

class BlackJackStats:
    """
    This class is a structured way of returning information about the outcome of playing many games of black jack, e.g., from play_games().
    Think of this as a C struct, where it is expected that data members will be direcly accessed, because this class has no methods, beyound __init__().
    """
    def __init__(self):
        """
        Create the data members of structured info.
            Dealer_Wins = The number of games won by the dealer, int
            Player_WIns = The number of games won by the player, int
            Pushes = The number of tie (push) games, int
        """
        self.Dealer_Wins = 0
        self.Player_Wins = 0
        self.Pushes = 0


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
    
    def set_player_play_strategy(self, ps = PlayStrategy()):
        """
        Set the player play strategy.
        :parameter ps: The player play strategy, PlayerPlayStrategy()
        :return: None
        """
        self.player_play_strategy = ps
        return None
            
    
    def set_dealer_play_strategy(self, ps = PlayStrategy()):
        """
        Set the dealer play strategy.
        :parameter ps: The dealer play strategy, PlayerPlayStrategy()
        :return: None
        """
        self.dealer_play_strategy = ps
        return None
                
    
    def switch_deck(self, new_deck = Deck(isInfinite = True)):
        """
        Replace the current deck with a new deck. Intended mainly to faciliatate testing, where it is helpful to use a StackedDeck().
        :parameter new_deck: The new Deck() to assign to the simulator, Deck()
        :return: None
        """
        self.deck = new_deck
        return None
        
    
    def draw_for_dealer(self, number=1):
        """
        Draw one or more cards from deck into dealer's hand.
        :parameter number: How many cards to draw into dealer's hand, int
        :return: A list of Card(s) in the hand after the draw
        """
        return self.dealer_hand.add_cards(self.deck.draw(number))
    
        
    def draw_for_player(self, number=1):
        """
        Draw one or more cards from deck into player's hand.
        :parameter number: How many cards to draw into player's hand, int
        :return: A list of Card(s) in the hand after the draw
        """
        return self.player_hand.add_cards(self.deck.draw(number))   
    
    
    def play_games(self, num_games = 1, player_deal = [], dealer_show = None):
        """
        Play multiple games of blackjack, returning a BlackJackStats() object of statistics of outcomes across the set of games.
        :parameter num_games: The number of games to play, int
        :parameter player_deal: A list of no, one, or two Card()s dealt to the player. The deal will be completed with 2, 1, or no
            cards. This is intended to enable fixing part or all of the initial player hand.
        :paremeter dealer_show: If specified, it is the showing, face up Card() for the dealer, and one additional card will be
            drawn to complete the dealer's initial hand. This is intended to enable fixing the part of the dealer's hand which
            is visible to the player.
        :return: Sstatistics for the set of games, as a BlackJackStats() object
        """
        game_stats = BlackJackStats()
        
        dealer_wins = 0
        player_wins = 0
        pushes = 0
        
        for g in range(num_games):  
            print('Playing game:', g)
            info = self.play_game(player_deal, dealer_show)
            if info.Game_Outcome == BlackJackGameOutcome.DEALER_WINS:
                dealer_wins += 1
            elif info.Game_Outcome == BlackJackGameOutcome.PLAYER_WINS:
                player_wins += 1
            elif info.Game_Outcome == BlackJackGameOutcome.PUSH:
                pushes += 1
        
        game_stats.Dealer_Wins = dealer_wins
        game_stats.Player_Wins = player_wins
        game_stats.Pushes = pushes
               
        return game_stats

    
    def play_game(self, player_deal = [], dealer_show = None):
        """
        Play one game of black jack, returning a GamePlayOutcome() object of information about the outcome of the game.
        :parameter player_deal: A list of no, one, or two Card()s dealt to the player. The deal will be completed with 2, 1, or no
            cards. This is intended to enable fixing part or all of the initial player hand.
        :paremeter dealer_show: If specified, it is the showing, face up Card() for the dealer, and one additional card will be
            drawn to complete the dealer's initial hand. This is intended to enable fixing the part of the dealer's hand which
            is visible to the player.
        :return: Information about the outcome of the game, GamePlayOutcome() object
        """
        info = GamePlayOutcome()
        
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
        if check_info == BlackJackCheck.PLAY_ON:
        
            # Neither dealer nor player have blackjack, on deal, so play the hands.
            
            # Play player hand, and add hand outcome info to game info
            player_info = self.play_player_hand()
            info.Player_Final_Hand = player_info.Final_Hand
            info.Player_Status = player_info.Status
            info.Player_Count = player_info.Count      
        
            # Play dealer hand, and add hand outcome info to game info
            dealer_info = self.play_dealer_hand()
            info.Dealer_Final_Hand = dealer_info.Final_Hand
            info.Dealer_Status = dealer_info.Status
            info.Dealer_Count = dealer_info.Count
                    
            # Determine game outcome, and add to game info
 
            self.determine_game_outcome(info)
         
        else:
            
            # One or both of dealer or/and player have blackjack. Set game outcome, etc. in game info

            info.Player_Final_Hand = str(self.player_hand)
            info.Dealer_Final_Hand = str(self.dealer_hand)
            
            if check_info == BlackJackCheck.BOTH_BLACKJACK:
                # It's a tie score, and a push
                info.Game_Outcome = BlackJackGameOutcome.PUSH
                info.Player_Status = BlackJackPlayStatus.BLACKJACK
                info.Player_Count = 21
                info.Dealer_Status = BlackJackPlayStatus.BLACKJACK
                info.Dealer_Count = 21
            elif check_info == BlackJackCheck.DEALER_BLACKJACK:
                info.Game_Outcome = BlackJackGameOutcome.DEALER_WINS
                info.Player_Status = BlackJackPlayStatus.NONE
                info.Player_Count = 0
                info.Dealer_Status = BlackJackPlayStatus.BLACKJACK
                info.Dealer_Count = 21
            elif check_info == BlackJackCheck.PLAYER_BLACKJACK:
                info.Game_Outcome = BlackJackGameOutcome.PLAYER_WINS
                info.Player_Status = BlackJackPlayStatus.BLACKJACK
                info.Player_Count = 21
                info.Dealer_Status = BlackJackPlayStatus.NONE
                info.Dealer_Count = 0

        return info
        
    
    def check_for_blackjack(self):
        """
        Check both the dealer's and player's hand for black jack, and declare a winner (one hand has blackjack) or a push (both hands have blackjack). 
        :return: The outcome of the black jack check, BlackJackCheck() enum
        """      
        
        # Note that this will be the default return, that is, if none of the if/elif below are true
        check_info = BlackJackCheck.PLAY_ON
        
        dealer_info = self.dealer_hand.hand_info()
        player_info = self.player_hand.hand_info()
        
        if dealer_info.Count_Max == 21 and player_info.Count_Max == 21:
            check_info = BlackJackCheck.BOTH_BLACKJACK
        elif dealer_info.Count_Max == 21:
            check_info = BlackJackCheck.DEALER_BLACKJACK
        elif player_info.Count_Max == 21:
            check_info = BlackJackCheck.PLAYER_BLACKJACK
            
        return check_info
    
    
    def play_dealer_hand(self):
        """
        Play the dealer's hand of black jack, using the dealer play strategy, and returning a HandPlayOutcome() object with
        information about the outcome of playing the hand.
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        outcome_info = self.dealer_play_strategy.play(self.dealer_hand, self.deck)
                  
        return outcome_info
        
 
    def play_player_hand(self):
        """
        Play the player's hand of black jack, using the player play strategy, and returning a HandPlayOutcome() object with
        information about the outcome of playing the hand.
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        # Get the first card in the dealer's hand, which is the face up card
        show = self.dealer_hand.get_cards()[0]
        
        outcome_info = self.player_play_strategy.play(self.player_hand, self.deck, show)
                    
        return outcome_info
    

    def determine_game_outcome(self, info = GamePlayOutcome()):
        """
        Complete the argument info dictionary after determing the game winner.
        Assumes that Player_Status, Dealer_Status, Player_Count, and Dealer_Count exist in the info dictionary upon entry to this method.
        :param info: Same info object returned by play_game(), GamePlayOutcome() object
        :return: NULL
        """
        if (info.Player_Status == BlackJackPlayStatus.BUST):
            # If player busts, then it doesn't matter what the dealer status is, the dealer wins.
            # This is the house's advantage in the game.
            info.Game_Outcome = BlackJackGameOutcome.DEALER_WINS
        elif (info.Player_Status == BlackJackPlayStatus.STAND) and (info.Dealer_Status == BlackJackPlayStatus.BUST):
            info.Game_Outcome = BlackJackGameOutcome.PLAYER_WINS
        else:
            # Both player and dealer stood, higher score wins
            if info.Player_Count > info.Dealer_Count:
                # Player wins
                info.Game_Outcome = BlackJackGameOutcome.PLAYER_WINS
            elif info.Player_Count < info.Dealer_Count:
                # Dealer wins
                info.Game_Outcome = BlackJackGameOutcome.DEALER_WINS
            else:
                # It's a tie score, and a push
                info.Game_Outcome = BlackJackGameOutcome.PUSH
       
        return None
    

