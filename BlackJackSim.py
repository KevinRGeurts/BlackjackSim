from asyncio.windows_events import NULL
from deck import Deck
from hand import Hand

class BlackJackSim(object):
    """
    Logic for playing a game of black jack.\n
    """

    def __init__(self):
        """
        Construct an infinite deck of Cards (i.e. an infinite deck shute), an empty dealer Hand, and an empty player Hand.
        """
        self.deck = Deck(isInfinite = True)
        self.dealer_hand = Hand()
        self.player_hand = Hand()
    
    # TODO: Enable ability to play a specified number of games and track/report statistics like % of different game outcomes across those games.
    # TODO: Add ability to log detailed results of all individual games in a set to a text file for later analyis.
    # TODO: Add a type of game play where the player and/or dealer hand has some consistent initial partial or full deal before play begins. (To simulate specific situations sitting at the table where the player can't see the dealer's second card and is curious about the odds.)    

    def play_game(self):
        """
        Play one game of black jack, returning a dictionary of information about the outcome of the game.
            Dealer_Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Dealer_Status = 'bust', 'stand', 'blackjack', or 'none' (player blackjacked, dealer didn't), string
            Dealer_Count = Final count of dealer's hand (0 if player blackjacked and dealer didn't), int
            Player_Final_Hand = String representation of Player's hand of cards at the end of the game, string
            Player_Status = 'bust', 'stand', 'blackjack', or 'none'  (dealer blackjacked, player didn't), string
            Player_Count = Final count of Player's hand (0 if dealer blackjacked and player didn't), int
            Game_Outcome = 'player wins', 'dealer wins', or 'push' (both blackjack, bust, or stand with a tie count)
        :return: Dictionary of information about the outcome of the game.
        """
        info = {}
        
        # Clear dealer and player hands of Cards
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        
        # Initial deal for dealer and player
        self.dealer_hand.add_cards(self.deck.draw(2))
        self.player_hand.add_cards(self.deck.draw(2))

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
 
            self.determine_game_outcome()
         
        else:
            
            # One or both of dealer or/and player have blackjack. Set game outcome, etc. in game info

            info['Player_Final_Hand'] = self.player_hand.print_hand()
            info['Dealer_Final_Hand'] = self.dealer_hand.print_hand()
            
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
        Play the dealer's hand of black jack, returning a dictionary of information about the outcome of the hand.
            Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Status = 'bust' or 'stand', string
            Count = Final count of dealer's hand, int
        :return: Dictionary of information about the outcome of the hand.
        """
        outcome_info = {}
        
        info = self.dealer_hand.hand_info()
        
        hand_status = ''
        final_count = 0
        # Hit as many times as needed until Count_Max exceeds 16
        while info['Count_Max'] <= 16:
            # Hit
            hand_status = 'hit'
            self.dealer_hand.add_cards(self.deck.draw(1))
            # print('Dealer Hand After Hitting on Max Count: ' + self.dealer_hand.print_hand())
            info = self.dealer_hand.hand_info()
            # print(info) 
        count_max = info['Count_Max']
        if (count_max >= 17) and (count_max <= 21):
            # Stand on Count_Max
            hand_status = 'stand'
            final_count = count_max
        elif count_max > 21:
            # We've busted on Count_Max, switch to Count_Min
            while info['Count_Min'] <= 16:
                # Hit
                hand_status = 'hit'
                self.dealer_hand.add_cards(self.deck.draw(1))
                # print('Dealer Hand After Hiting on Count_Min: ' + self.dealer_hand.print_hand())
                info = self.dealer_hand.hand_info()
                # print(info)
            count_min = info['Count_Min']
            if (count_min >= 17) and (count_min <= 21):
                # Stand on Count_Min
                hand_status = 'stand'
                final_count = count_min
            elif count_min > 21:
                # If we've busted on Count_Min, and the hand
                hand_status = 'bust'
                final_count = count_min
        # print('Dealer Hand Outcome:', hand_status, final_count)

        # Assemble outcome info for the hand
        outcome_info['Final_Hand'] = self.dealer_hand.print_hand()
        outcome_info['Status'] = hand_status
        outcome_info['Count'] = final_count
            
        return outcome_info
        
    # TODO: Create another play_player_hand using player guidelines from Hoyle.
    # TODO: Implement a design pattern allowing abstraction and swapping out of playing rules for player and possibly dealer.
    
    def play_player_hand(self):
        """
        Play the player's hand of black jack, returning a dictionary of information about the outcome of the hand.
            Final_Hand = String representation of player's hand of cards at the end of the game, string
            Status = 'bust' or 'stand', string
            Count = Final count of player's hand, int
        *** Play logic is currently the same as for dealer, which is not the ultimate goal, and is likely to end up with
        a poor outcome statistically for the player, since the player will tend to bust first due to order of play when using same logic. ***
        :return: Dictionary of information about the outcome of the hand.
        """
        outcome_info = {}
        
        info = self.player_hand.hand_info()
        
        hand_status = ''
        final_count = 0
        # Hit as many times as needed until Count_Max exceeds 16
        while info['Count_Max'] <= 16:
            # Hit
            hand_status = 'hit'
            self.player_hand.add_cards(self.deck.draw(1))
            # print('Player Hand After Hitting on Max Count: ' + self.player_hand.print_hand())
            info = self.player_hand.hand_info()
            # print(info) 
        count_max = info['Count_Max']
        if (count_max >= 17) and (count_max <= 21):
            # Stand on Count_Max
            hand_status = 'stand'
            final_count = count_max
        elif count_max > 21:
            # If we've busted on Count_Max, switch to Count_Min
            while info['Count_Min'] <= 16:
                # Hit
                hand_status = 'hit'
                self.player_hand.add_cards(self.deck.draw(1))
                # print('Player Hand After Hiting on Count_Min: ' + self.player_hand.print_hand())
                info = self.player_hand.hand_info()
                # print(info)
            count_min = info['Count_Min']
            if (count_min >= 17) and (count_min <= 21):
                # Stand on Count_Min
                hand_status = 'stand'
                final_count = count_min
            elif count_min > 21:
                # We've busted on Count_Min, and the hand
                hand_status = 'bust'
                final_count = count_min
        # print('Player Hand Outcome:', hand_status, final_count)

        # Assemble outcome info for the hand
        outcome_info['Final_Hand'] = self.player_hand.print_hand()
        outcome_info['Status'] = hand_status
        outcome_info['Count'] = final_count
            
        return outcome_info
    

    def determine_game_outcome(self, info = {}):
        """
        Complete the argument info dictionary after determing the game winner.
        Assumes that Player_Status, Dealer_Status, Player_Count, and Dealer_Count exist in the info dictionary upon entry to this method.
        :param info: same info object returned by play_game(), dictionary
        :return: NULL
        """
        if (info['Player_Status']) == 'stand' and (info['Dealer_Status'] == 'bust'):
            info['Game_Outcome'] = 'player wins'
        elif (info['Player_Status']) == 'bust' and (info['Dealer_Status'] == 'stand'):
            info['Game_Outcome'] = 'dealer wins'
        elif (info['Player_Status']) == 'stand' and (info['Dealer_Status'] == 'stand'):
            # Higher score wins
            if info['Player_Count'] > info['Dealer_Count']:
                # Player wins
                info['Game_Outcome'] = 'player wins'
            elif info['Player_Count'] < info['Dealer_Count']:
                # Dealer wins
                info['Game_Outcome'] = 'dealer wins'
            else:
                # It's a tie score, and a push
                info['Game_Outcome'] = 'push'
        else:
            # Both player and dealer busted, so its a push
            info['Game_Outcome'] = 'push'
       
        return NULL;
    

