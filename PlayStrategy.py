from hand import Hand
from deck import Deck

class PlayStrategy:
    """
    Following a Strategy design pattern, this is the interface class for all blackjack hand playing strategies.
    It litteraly defines no attributes or methods. By convention (and necessity) each child must define a play(...) method.
    """   
 
class CasinoDealerPlayStrategy(PlayStrategy):
    """
    Implements strategy for (casino) dealer play.
    """
    
    def play(self, hand = Hand(), deck = Deck()):
        """
        The method called to invoke the hand playing strategy.
        Play the dealer's hand of black jack, returning a dictionary of information about the outcome of the hand.
            Final_Hand = String representation of dealer's hand of cards at the end of the game, string
            Status = 'bust' or 'stand', string
            Count = Final count of dealer's hand, int
        :parameter hand: The Hand to be played.
        :parameter deck: The Deck from which to draw cards.
        :return: Dictionary of information about the outcome of the hand. 
        """
        outcome_info = {}
        
        info = hand.hand_info()
        
        hand_status = ''
        final_count = 0
        # Hit as many times as needed until Count_Max exceeds 16
        while info['Count_Max'] <= 16:
            # Hit
            hand_status = 'hit'
            hand.add_cards(deck.draw(1))
            # print('Dealer Hand After Hitting on Max Count: ' + hand.print_hand())
            info = hand.hand_info()
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
                hand.add_cards(deck.draw(1))
                # print('Dealer Hand After Hiting on Count_Min: ' + hand.print_hand())
                info = hand.hand_info()
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
        outcome_info['Final_Hand'] = hand.print_hand()
        outcome_info['Status'] = hand_status
        outcome_info['Count'] = final_count
            
        return outcome_info

