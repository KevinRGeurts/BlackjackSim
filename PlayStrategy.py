from enum import Enum


class BlackJackPlayStatus(Enum):
    """
    An enumeration that is part of the object that represents the outcome of a hand in a game.
    """
    HIT = 1
    STAND = 2
    BUST = 3
    BLACKJACK = 4
    # NONE used if the other game participant blackjacked and this participant didn't.
    # NONE also used for the second hand of a split pair if their was not split.
    NONE = 5


class HandPlayOutcome:
    """
    This class is a structured way of returning information about the outcome of playing a hand play().
    Think of this as a C struct, where it is expected that data members will be direcly accessed, because this class has no methods, beyound __init__().
    """
    def __init__(self):
        """
        Create the data members of structured info.
            Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Status = Was the outcome of playing the hand Stand or Bust?, BlackJackPlayStatus enum 
            Count = Final count of dealer's hand, int
        """
        self.Final_Hand = ''
        self.Status = BlackJackPlayStatus.STAND
        self.Count = 0


class PlayStrategy:
    """
    Following a Strategy design pattern, this is the interface class for all blackjack hand playing strategies.
    Each child must by convention and necessity implement these methods:
        play(...) - For playing a hand following the strategy
        split(...) - For answering True or False to the question of if a split is desired when a pair has been dealt
    """


class CasinoDealerPlayStrategy(PlayStrategy):
    """
    Implements strategy for (casino) dealer play.
    """
    
    def split(self, pair_pips = '', dealer_show_pips = ''):
        """
        The method called to determine if the strategy calls for a split after a pair of cards is dealt. This should always return False.
        :parameter pair_pips: The pips string of the pair of Cards dealt to the player, string
        :parameter dealer_show_pips: The pips string of the dealer's face up show card, string
        :return: True if should split, False if should NOT split, Boolean
        """
        # No splits for this play strategy, so return False
        return False
    
    
    # Note: First attempt was the following argument list, but having to import BlackJackSim caused a circular import problem.
    # def play(self, hand_info_callback = BlackJackSim.player_hand_info, draw_callback = BlackJackSim.draw_for_player, dealer_show_callback = BlackJackSim.get_dealer_show):
    # TODO: It would be nice if there was a way to check if the X_callback arguments are actually bound methods. But googling has not suggested a workable solution.
    def play(self, hand_info_callback, draw_callback, dealer_show_callback):
        """
        The method called to invoke the hand playing strategy.
            (1) Hit on <= 16
            (2) Stand on >= 17
        Play the hand of black jack, returning a HandPlayOutcome() object with information about the outcome of playing the hand.
        :parameter hand_info_callback: Bound method used by the strategy to obtain required info about the hand being played, e.g., BlackJackSim.dealer_hand_info
        :parameter draw_callback: Bound method used by the strategy to draw cards into the hand being played, e.g., BlackJackSim.draw_for_dealer
        :parameter dealer_show_callback: Bound method used by the strategy to obtain the dealer's face up show card, e.g., BlackJackSim.get_dealer_show
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        outcome_info = HandPlayOutcome()
        
        info = hand_info_callback()
        
        hand_status = BlackJackPlayStatus.STAND
        final_count = 0
        # Hit as many times as needed until Count_Max exceeds 16
        while info.Count_Max <= 16:
            # Hit
            hand_status = BlackJackPlayStatus.HIT
            draw_callback(1)
            # print('Dealer Hand After Hitting on Max Count: ', hand)
            info = hand_info_callback()
            # print(info) 
        count_max = info.Count_Max
        if (count_max >= 17) and (count_max <= 21):
            # Stand on Count_Max
            hand_status = BlackJackPlayStatus.STAND
            final_count = count_max
        elif count_max > 21:
            # We've busted on Count_Max, switch to Count_Min
            while info.Count_Min <= 16:
                # Hit
                hand_status = BlackJackPlayStatus.HIT
                draw_callback(1)
                # print('Dealer Hand After Hiting on Count_Min: ', hand)
                info = hand_info_callback()
                # print(info)
            count_min = info.Count_Min
            if (count_min >= 17) and (count_min <= 21):
                # Stand on Count_Min
                hand_status = BlackJackPlayStatus.STAND
                final_count = count_min
            elif count_min > 21:
                # If we've busted on Count_Min, and the hand
                hand_status = BlackJackPlayStatus.BUST
                final_count = count_min
        # print('Dealer Hand Outcome:', hand_status, final_count)

        # Assemble outcome info for the hand
        outcome_info.Final_Hand = info.String_Rep
        outcome_info.Status = hand_status
        outcome_info.Count = final_count
            
        return outcome_info


class InteractivePlayerPlayStrategy(PlayStrategy):
    """
    Implements strategy for player play, based on asking a human whether to hit or stand.
    Human is also asked if the want to split a dealt pair.
    """
    
    def split(self, pair_pips = '', dealer_show_pips = ''):
        """
        The method called to determine if the strategy calls for a split after a pair of cards is dealt. This should
        :parameter pair_pips: The pips string of the pair of Cards dealt to the player, string
        :parameter dealer_show_pips: The pips string of the dealer's face up show card, string
        :return: True if should split, False if should NOT split, Boolean
        """
        # We're interactive here, so ask the user if they want to split
        response = input('Do you wish to split your pair of ' + pair_pips + ' ? Dealer shows ' + dealer_show_pips + '. (Y/N)?')
        if response == 'Y' or response == 'y':
            return True
        else:
            return False
    
    
    # Note: First attempt was the following argument list, but having to import BlackJackSim caused a circular import problem.
    # def play(self, hand_info_callback = BlackJackSim.player_hand_info, draw_callback = BlackJackSim.draw_for_player, dealer_show_callback = BlackJackSim.get_dealer_show):
    # TODO: It would be nice if there was a way to check if the X_callback arguments are actually bound methods. But googling has not suggested a workable solution.
    def play(self, hand_info_callback, draw_callback, dealer_show_callback):
        """
        The method called to invoke the hand playing strategy.
        Play the hand of black jack, returning a HandPlayOutcome() object of information about the outcome of the hand.
        :parameter hand_info_callback: Bound method used by the strategy to obtain required info about the hand being played, e.g., BlackJackSim.player_hand_info
        :parameter draw_callback: Bound method used by the strategy to draw cards into the hand being played, e.g., BlackJackSim.draw_for_player
        :parameter dealer_show_callback: Bound method used by the strategy to obtain the dealer's face up show card, e.g., BlackJackSim.get_dealer_show
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        outcome_info = HandPlayOutcome()
        
        hand_status = BlackJackPlayStatus.HIT
        final_count = 0
        
        info = hand_info_callback()       
        
        print('Playing an interactive hand of blackjack...')
        print('Player''s hand:', info.String_Rep, '     Dealer shows:', str(dealer_show_callback()))
        response = input('(H)it or (S)tand?')
        while response == 'H' or response == 'h':
            draw_callback(1)
            info = hand_info_callback()
            if info.Count_Min > 21:
                hand_status = BlackJackPlayStatus.BUST
                final_count = info.Count_Min
                break
            print('Player''s hand:', info.String_Rep, '     Dealer shows:', str(dealer_show_callback()))
            response = input('(H)it or (S)tand?')
        
        hand_status = BlackJackPlayStatus.STAND
        final_count =  info.Count_Max
        if final_count > 21:
            final_count = info.Count_Min
                
        # Assemble outcome info for the hand
        outcome_info.Final_Hand = info.String_Rep
        outcome_info.Status = hand_status
        outcome_info.Count = final_count
            
        return outcome_info    



class HoylePlayerPlayStrategy(PlayStrategy):
    """
    Implements strategy for player play and splitting a dealt pair, based on recommendations in Hoyle's Rules of Games.
    """

    def split(self, pair_pips = '', dealer_show_pips = ''):
        """
        The method called to determine if the strategy calls for a split after a pair of cards is dealt.
            (1) Always split A's or 8's.
            (2) Never split A's. (Desirable for a user to split A's, but not allowed by most casinos.)
            (3) Never split Face cards, 10's, 5's, 4's
            (4) Split other pairs unless dealer shows 7+ or an A
        :parameter pair_pips: The pips string of the pair of Cards dealt to the player, string
        :parameter dealer_show_pips: The pips string of the dealer's face up show card, string
        :return: True if should split, False if should NOT split, Boolean
        """
        # Apply the reccomendations from Hoyle to determine if a split is desired
        should_split = False
        match pair_pips:
            case '8':
                # Always split 8's
                should_split = True
            case 'A':
                # Splitting Aces is desirable for player, but not allowed by casino rules
                should_split = False
            case 'K' | 'Q' | 'J' | '10' | '5' | '4':
                # Never split face cards, 10's, 5's, or 4's
                should_split = False
            case '9' | '7' | '6' | '3' | '2':
                # Split unless dealer shows 7+ or Ace
                match dealer_show_pips:
                    case '7' | '8' | '9' | '10' | 'J' | 'Q' | 'K' | 'A':
                        should_split = False
                    case '2' | '3' | '4' | '5' | '6':
                        should_split = True
        return should_split


	# Check Count_Max
	# 	If Count_Max > 17 and <= 21, then stand [done]
	# 	If Count_Max <= 17 or > 21, then
	# Check Count_Min
	# 	If Count_Min > 21, then bust [done]
	# 	If Count_Min >= 17, then stand [done]
	# 	If Count_Min <= 12, then hit [done]
	# 	If Count_Min >=13 and <= 16, then
	# 		If dealer shows <= 6 (their one face up card), then stand (expecting dealer to hit and bust) [done]
	# 		If dealer shows 7 - 10, J, Q, K, A, then hit [done]
	# After hitting, return to Check Count_Max [done]    
    
    # Note: First attempt was the following argument list, but having to import BlackJackSim caused a circular import problem.
    # def play(self, hand_info_callback = BlackJackSim.player_hand_info, draw_callback = BlackJackSim.draw_for_player, dealer_show_callback = BlackJackSim.get_dealer_show):
    # TODO: It would be nice if there was a way to check if the X_callback arguments are actually bound methods. But googling has not suggested a workable solution.
    def play(self, hand_info_callback, draw_callback, dealer_show_callback):
        """
        The method called to invoke the hand playing strategy.
        Play the hand of black jack, returning a HandPlayOutcome() object of information about the outcome of the hand.
        :parameter hand_info_callback: Bound method used by the strategy to obtain required info about the hand being played, e.g., BlackJackSim.dealer_hand_info
        :parameter draw_callback: Bound method used by the strategy to draw cards into the hand being played, e.g., BlackJackSim.draw_for_dealer
        :parameter dealer_show_callback: Bound method used by the strategy to obtain the dealer's face up show card, e.g., BlackJackSim.get_dealer_show
        :return: Information about the outcome of playing the hand, HandPlayOutcome() class object
        """
        outcome_info = HandPlayOutcome()
        
        hand_status = BlackJackPlayStatus.HIT
        final_count = 0
        
        while hand_status == BlackJackPlayStatus.HIT:
        
            info = hand_info_callback()
            
            if info.Count_Max <= 17 or info.Count_Max > 21:
                # Need to check Count_Min
                if info.Count_Min > 21:
                    # Bust
                    hand_status = BlackJackPlayStatus.BUST
                    final_count = info.Count_Min
                elif info.Count_Min >= 17:
                    # Stand
                    hand_status = BlackJackPlayStatus.STAND
                    final_count = info.Count_Min
                elif info.Count_Min <= 12:
                    # Hit
                    hand_status = BlackJackPlayStatus.HIT
                    draw_callback(1)
                else:
                    # Hand counts between 13 and 16 inclusive. Decide to hit or stand based on dealer's face up card.
                    if dealer_show_callback().count_card(ace_high = True) <= 6:
                        # Dealer shows 2 - 6, so stand (hoping dealer will have to hit and will bust)
                        hand_status = BlackJackPlayStatus.STAND
                        final_count = info.Count_Min
                    else:
                        # Dealer shows 7 - 10, J, Q, K, or A, so hit
                        hand_status = BlackJackPlayStatus.HIT
                        draw_callback(1)
            else:
                # Stand, because Count_Max is > 17, and we haven't busted
                hand_status = BlackJackPlayStatus.STAND
                final_count = info.Count_Max
                
        # Assemble outcome info for the hand
        outcome_info.Final_Hand = info.String_Rep
        outcome_info.Status = hand_status
        outcome_info.Count = final_count
            
        return outcome_info


