from asyncio.windows_events import NULL
from deck import Deck
from hand import Hand
from PlayStrategy import BlackJackPlayStatus, PlayStrategy, CasinoDealerPlayStrategy, HoylePlayerPlayStrategy
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
    # NONE means that the hand used to play the second hand of a split pair was not used in the game, that is, no pair was split
    NONE = 4


class GamePlayOutcome:
    """
    This class is a structured way of returning information about the outcome of playing a game of black jack, e.g., from play_game().
    Think of this as a C struct, where it is expected that data members will be direcly accessed, because this class has no methods, beyound __init__().
    """
    def __init__(self):
        """
        Create the data members of structured info.
            Dealer_Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Dealer_Status = 'bust', 'stand', 'blackjack', or 'none' (player blackjacked, dealer didn't), BlackJackPlayStatus Enum
            Dealer_Count = Final count of dealer's hand (0 if player blackjacked and dealer didn't), int
            Player_Final_Hand = String representation of Player's hand of cards at the end of the game, string
            Player_Status = 'bust', 'stand', 'blackjack', or 'none'  (dealer blackjacked, player didn't), BlackJackPlayStatus Enum
            Player_Count = Final count of Player's hand (0 if dealer blackjacked and player didn't), int
            Split_Final_Hand = String representation of Player's split hand of cards at the end of the game, string
                (Empty if player's hand is not split.)
            Split_Status = 'bust', 'stand', 'blackjack', or 'none'  (dealer blackjacked, player didn't), BlackJackPlayStatus Enum
                ('none' if player's hand is not split.)
            Split_Count = Final count of Player's split hand (0 if dealer blackjacked and player didn't), int
                (0 if player's hand is not split.)
            Game_Outcome = Who won?, BlackJackGameOutcome() enum
            Split_Game_Outcome = Who won the split game?, BlackJackGameOutcome() enum
        """
        self.Dealer_Final_Hand = ''
        self.Dealer_Status = BlackJackPlayStatus.STAND
        self.Dealer_Count = 0
        self.Player_Final_Hand = ''
        self.Player_Status = BlackJackPlayStatus.STAND
        self.Player_Count = 0
        self.Split_Final_Hand = ''
        self.Split_Status = BlackJackPlayStatus.NONE
        self.Split_Count = 0
        self.Game_Outcome = BlackJackGameOutcome.PUSH
        self.Split_Game_Outcome = BlackJackGameOutcome.NONE
    

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
            Dealer_BlackJacks = The number of games where the dealer was dealt BlackJack, int
            Player_BlackJacks = The number of games where teh player was dealt BlackJack, int
            Notes:
                If a dealer is dealt BlackJack, then Dealer_Wins +=1 and Dealer_BlackJacks +=1
                If a player is dealt BlackJack, and the Dealer isn't, then Player_Wins +=1, and Player_BlackJacks +=1
                If both player and dealer are dealt BlackJack, then Pushes +=1, Dealer_BlackJacks +=1, PlayerBlackJacks +=1
        """
        self.Dealer_Wins = 0
        self.Player_Wins = 0
        self.Pushes = 0
        self.Dealer_BlackJacks = 0
        self.Player_BlackJacks = 0


# TODO: If we only defaulted play strategies to PlayStrategy, we wouldn't need to import the specific implementations, which
# would probably be more consistent with the intent of abstraction
class BlackJackSim:
    """
    Logic for playing a game of black jack.\n
    """

    def __init__(self):
        """
        Construct an infinite deck of Cards (i.e. an infinite deck shute), an empty dealer Hand, an empty player Hand,
        and, to be used if needed, an empty hand for if the player splits a pair.
        """
        self.deck = Deck(isInfinite = True)
        self.dealer_hand = Hand()
        self.dealer_play_strategy = CasinoDealerPlayStrategy()
        self.player_hand = Hand()
        self.split_hand = Hand() # For if the player splits a pair
        self.player_play_strategy = HoylePlayerPlayStrategy()
        
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
    
    
    def dealer_hand_info(self):
        """
        Call Hand.hand_info on the dealer's hand.
        :return: Hand.HandInfo object with useful information about the dealer's hand.
        """
        return self.dealer_hand.hand_info()
    

    def player_hand_info(self):
        """
        Call Hand.hand_info on the player's hand.
        :return: Hand.HandInfo object with useful information about the player's hand.
        """
        return self.player_hand.hand_info()


    def split_hand_info(self):
        """
        Call Hand.hand_info on the player's split hand.
        :return: Hand.HandInfo object with useful information about the player's split hand.
        """
        return self.split_hand.hand_info()    
        
    
    def draw_for_player(self, number=1):
        """
        Draw one or more cards from deck into player's hand.
        :parameter number: How many cards to draw into player's hand, int
        :return: A list of Card(s) in the hand after the draw
        """
        return self.player_hand.add_cards(self.deck.draw(number))
    
    
    def draw_for_split(self, number=1):
        """
        Draw one or more cards from deck into player's split hand.
        :parameter number: How many cards to draw into player's split hand, int
        :return: A list of Card(s) in the hand after the draw
        """
        return self.split_hand.add_cards(self.deck.draw(number))   
    
    
    def get_dealer_show(self):
        """
        Return the dealer's face up (show) card that can be seen by the player.
        :return: The first card in the dealer's hand, Card()
        """
        return self.dealer_hand.get_cards()[0]
    
    
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
        dealer_blackjacks = 0
        player_blackjacks = 0
        
        for g in range(num_games):  
            print('Playing game:', g)
            info = self.play_game(player_deal, dealer_show)
            # Gather and record stats on who won
            if info.Game_Outcome == BlackJackGameOutcome.DEALER_WINS:
                dealer_wins += 1
            elif info.Game_Outcome == BlackJackGameOutcome.PLAYER_WINS:
                player_wins += 1
            elif info.Game_Outcome == BlackJackGameOutcome.PUSH:
                pushes += 1
            # Gather and record stats on who won the split hand if the player split a pair
            if info.Split_Game_Outcome == BlackJackGameOutcome.DEALER_WINS:
                dealer_wins += 1
            elif info.Split_Game_Outcome == BlackJackGameOutcome.PLAYER_WINS:
                player_wins += 1
            elif info.Split_Game_Outcome == BlackJackGameOutcome.PUSH:
                pushes += 1
            # Gather and record stats on getting BlackJack
            if info.Dealer_Status == BlackJackPlayStatus.BLACKJACK:
                dealer_blackjacks += 1
            if info.Player_Status == BlackJackPlayStatus.BLACKJACK:
                player_blackjacks += 1
            if info.Split_Status == BlackJackPlayStatus.BLACKJACK:
                player_blackjacks += 1
        
        game_stats.Dealer_Wins = dealer_wins
        game_stats.Player_Wins = player_wins
        game_stats.Pushes = pushes
        game_stats.Dealer_BlackJacks = dealer_blackjacks
        game_stats.Player_BlackJacks = player_blackjacks
               
        return game_stats

    
    def play_game(self, player_deal = [], dealer_show = None, dealer_down = None):
        """
        Play one game of black jack, returning a GamePlayOutcome() object of information about the outcome of the game.
        :parameter player_deal: A list of no, one, or two Card()s dealt to the player. The deal will be completed with 2, 1, or no
            cards. This is intended to enable fixing part or all of the initial player hand.
        :parameter dealer_show: If specified, it is the showing, face up Card() for the dealer, and one additional card will be
            drawn to complete the dealer's initial hand. This is intended to enable fixing the part of the dealer's hand which
            is visible to the player.
        :parameter dealer_down: If specified, it is the face down Card() for the dealer. This is intended to fix the part of the
            dealer's deal that is invisible to the player.
        :return: Information about the outcome of the game or games (if their is a split), GamePlayOutcome() object
        """
        info = GamePlayOutcome()
        
        # Clear dealer, player, and split hands of Cards
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        self.split_hand = Hand()
        
        # TODO: Simplify this logic, using 'not (is None)' syntax
        # Build the dealer's initial hand, drawing as needed
        if dealer_show is None and dealer_down is None:
            self.dealer_hand.add_cards(self.deck.draw(2))
        elif dealer_show is None:
            self.dealer_hand.add_cards(dealer_down)
            self.dealer_hand.add_cards(self.deck.draw(1))
        elif dealer_down is None:
            self.dealer_hand.add_cards(dealer_show)
            self.dealer_hand.add_cards(self.deck.draw(1))
        else:
             self.dealer_hand.add_cards(dealer_show)
             self.dealer_hand.add_cards(dealer_down)
            
        # Build the player's inital hand, drawing as needed
        assert(len(player_deal) <=2)
        self.player_hand.add_cards(player_deal)
        if len(player_deal) == 0:
            self.player_hand.add_cards(self.deck.draw(2))
        elif len(player_deal) == 1:
            self.player_hand.add_cards(self.deck.draw(1))
        
        check_info = self.check_for_blackjack()
        if check_info == BlackJackCheck.PLAY_ON:
        
            # Neither dealer nor player have blackjack, on deal, so play the hands.

            if self.player_hand.get_cards()[0].get_pips() == self.player_hand.get_cards()[1].get_pips():
                # The player has been dealt a pair. Ask the player strategy if we should split.
                print('Player has a pair and could split: ', str(self.player_hand), 'Dealer shows: ', self.get_dealer_show().get_pips())
                if self.player_play_strategy.split(self.player_hand.get_cards()[0].get_pips(), self.get_dealer_show().get_pips()):
                    print('Player chose to split.')
                    # Execute split
                    # TODO: Don't reach directly into Hand members
                    
                    # Preserve second of pair to be transferred to split hand, and remove it from the player's hand
                    xfer_card = self.player_hand.cards.pop()
                    # Add the preserved card to the split hand
                    self.split_hand.add_cards([xfer_card])
                    # Draw a second card into the split hand
                    self.draw_for_split(1)
                    # TODO: What if we drew to BlackJack in the split?
                    
                    # Draw a replacement card for the player's hand
                    self.draw_for_player(1)
                    # TODO: What if we drew to BlackJack in the player's hand?
                    
                    # Play the split hand, and add hand outcome info to game info

                    split_info = self.play_split_hand()
                    info.Split_Final_Hand = split_info.Final_Hand
                    info.Split_Status = split_info.Status
                    info.Split_Count = split_info.Count 

            
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
        outcome_info = self.dealer_play_strategy.play(hand_info_callback=self.dealer_hand_info, draw_callback=self.draw_for_dealer, dealer_show_callback=self.get_dealer_show)
                  
        return outcome_info
        
 
    def play_player_hand(self):
        """
        Play the player's hand of black jack, using the player play strategy, and returning a HandPlayOutcome() object with
        information about the outcome of playing the hand.
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        outcome_info = self.player_play_strategy.play(hand_info_callback=self.player_hand_info, draw_callback=self.draw_for_player, dealer_show_callback=self.get_dealer_show)
                    
        return outcome_info
    
    
    def play_split_hand(self):
        """
        Play the player's split hand of black jack, using the player play strategy, and returning a HandPlayOutcome() object with
        information about the outcome of playing the hand.
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        outcome_info = self.player_play_strategy.play(hand_info_callback=self.split_hand_info, draw_callback=self.draw_for_split, dealer_show_callback=self.get_dealer_show)

        return outcome_info
    

    def determine_game_outcome(self, info = GamePlayOutcome()):
        """
        Complete the argument info dictionary after determing the game winner.
        Assumes that Player_Status, Dealer_Status, Player_Count, and Dealer_Count exist in the info dictionary upon entry to this method.
        Assumes that Split_Count exists upon entry to this method if Split_Status != BlackJackPlayStatus.NONE
        :param info: Same info object returned by play_game(), GamePlayOutcome() object
        :return: NULL
        """
        # Determine game outcome for the only hand of the game, or for the first hand if there was a split of a pair by player
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
                
        # Determine game outcome for the second, split hand, if there was a split of a pair by the player
        if (info.Split_Status != BlackJackPlayStatus.NONE):
            if (info.Split_Status == BlackJackPlayStatus.BUST):
                # If split busts, then it doesn't matter what the dealer status is, the dealer wins.
                # This is the house's advantage in the game.
                info.Split_Game_Outcome = BlackJackGameOutcome.DEALER_WINS
            elif (info.Split_Status == BlackJackPlayStatus.STAND) and (info.Dealer_Status == BlackJackPlayStatus.BUST):
                info.Split_Game_Outcome = BlackJackGameOutcome.PLAYER_WINS
            else:
                # Both split and dealer stood, higher score wins
                if info.Split_Count > info.Dealer_Count:
                    # Split wins
                    info.Split_Game_Outcome = BlackJackGameOutcome.PLAYER_WINS
                elif info.Split_Count < info.Dealer_Count:
                    # Dealer wins
                    info.Split_Game_Outcome = BlackJackGameOutcome.DEALER_WINS
                else:
                    # It's a tie score, and a push
                    info.Split_Game_Outcome = BlackJackGameOutcome.PUSH         
       
        return None
    

