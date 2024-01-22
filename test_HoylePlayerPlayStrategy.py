import unittest
from BlackJackSim import BlackJackSim
from PlayStrategy import BlackJackPlayStatus, HoylePlayerPlayStrategy
from deck import Stacked_Deck
from card import Card

class Test_HoylePlayerPlayStrategy(unittest.TestCase):
    # Check Count_Max
	# 	If Count_Max > 17 and <= 21, then stand [A 7] Test 1
	# 	If Count_Max <= 17 or > 21, then check Count_Min [A 6]; [A 6 5] Test 2
	# Check Count_Min
	# 	If Count_Min > 21, then bust [A 6 5 K] Test 2
	# 	If Count_Min >= 17, then stand [A 6 5 7] Test 3
	# 	If Count_Min <= 12, then hit [A 6 5] Test 2, Test 3
	# 	If Count_Min >=13 and <= 16, then [A 6 5 2] Test 4
	# 		If dealer shows <= 6 (their one face up card), then stand (expecting dealer to hit and bust) [show = 6] Test 4
	# 		If dealer shows 7 - 10, J, Q, K, A, then hit [A 6 5 2 3] [show = 7] Test 5
	# After hitting, return to Check Count_Max

	# Construct the following test cases
	# Test 1 "stand max": Hand[A 7] Deck[...] show[...] Stand
	# Test 2 "bust min": Hand[A 6] Deck[5 K] show[...] Hit Hit Bust
	# Test 3 "stand min over seventeen": Hand[A 6] Deck[5 7] show[...] Hit Hit Stand
	# Test 4 "stand min on show six or under": Hand[A 6] Deck[5 2] show[6] Hit Hit Stand
	# Test 5 "stand min on show over six": Hand[A 6] Deck[5 2 3] show[7] Hit Hit Hit Stand   
    
    def test_play_stand_max(self):
        
        # Create the sim object which will provide hand and deck for the play strategy
        bjs = BlackJackSim()
        
        # Create the desired play strategy for the test
        ps = HoylePlayerPlayStrategy()
       
        # Create a Stacked_Deck.
        # The first two cards will end up in the player's hand.
        # The third card will end up in the dealer's hand, so there is a show card available.
        # The rest don't matter as there should be no draws during play.
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','7'), Card('S','5'), Card('H','2')])
        
        # Assign the created deck to the sim object
        bjs.switch_deck(sd)
        
        # Add cards to the player's hand in the sim
        bjs.draw_for_player(2)
        
        # Add show card to dealer's hand in the sim
        bjs.draw_for_dealer(1)
        
        # Play the hand
        info = ps.play(bjs.player_hand_info, bjs.draw_for_player, bjs.get_dealer_show)
        
        # Do we have the expected final hand?
        exp_val = 'AC 7D'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.STAND
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 18
        act_val = info.Count
        self.assertEqual(exp_val, act_val)


    def test_play_bust_min(self):

        # Create the sim object which will provide hand and deck for the play strategy
        bjs = BlackJackSim()
                
        ps = HoylePlayerPlayStrategy()
        
        # Create a Stacked_Deck.
        # Card 1, 2, 4, 5 will end up in the player's hand.
        # Card 3 will end up in the dealer's hand, so there is a show card available.

        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','6'), Card('S','10'), Card('S','5'), Card('H','K')])

        # Assign the created deck to the sim object
        bjs.switch_deck(sd)
        
        # Add cards to the player's hand in the sim
        bjs.draw_for_player(2)
        
        # Add show card to dealer's hand in the sim
        bjs.draw_for_dealer(1)
        
        # Play the hand
        info = ps.play(bjs.player_hand_info, bjs.draw_for_player, bjs.get_dealer_show)
        
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S KH'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.BUST
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 22
        act_val = info.Count
        self.assertEqual(exp_val, act_val)

    
    def test_play_stand_min_over_seventeen(self):
        
        # Create the sim object which will provide hand and deck for the play strategy
        bjs = BlackJackSim()
                
        ps = HoylePlayerPlayStrategy()
        
        # Create a Stacked_Deck.
        # Card 1, 2, 4, 5 will end up in the player's hand.
        # Card 3 will end up in the dealer's hand, so there is a show card available.

        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','6'), Card('S','10'), Card('S','5'), Card('H','7')])

        # Assign the created deck to the sim object
        bjs.switch_deck(sd)
        
        # Add cards to the player's hand in the sim
        bjs.draw_for_player(2)
        
        # Add show card to dealer's hand in the sim
        bjs.draw_for_dealer(1)
        
        # Play the hand
        info = ps.play(bjs.player_hand_info, bjs.draw_for_player, bjs.get_dealer_show)
        
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S 7H'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.STAND
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 19
        act_val = info.Count
        self.assertEqual(exp_val, act_val)


    def test_play_stand_min_on_show_six_or_under(self):
         
        # Create the sim object which will provide hand and deck for the play strategy
        bjs = BlackJackSim()
                
        ps = HoylePlayerPlayStrategy()
        
        # Create a Stacked_Deck.
        # Card 1, 2, 4, 5 will end up in the player's hand.
        # Card 3 will end up in the dealer's hand, so there is a show card available.

        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','6'), Card('S','6'), Card('S','5'), Card('H','2')])

        # Assign the created deck to the sim object
        bjs.switch_deck(sd)
        
        # Add cards to the player's hand in the sim
        bjs.draw_for_player(2)
        
        # Add show card to dealer's hand in the sim
        bjs.draw_for_dealer(1)
        
        # Play the hand
        info = ps.play(bjs.player_hand_info, bjs.draw_for_player, bjs.get_dealer_show)
       
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S 2H'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.STAND
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 14
        act_val = info.Count
        self.assertEqual(exp_val, act_val)

 
    def test_play_stand_min_on_show_over_six(self):
        
        # Create the sim object which will provide hand and deck for the play strategy
        bjs = BlackJackSim()
                
        ps = HoylePlayerPlayStrategy()
        
        # Create a Stacked_Deck.
        # Card 1, 2, 4, 5, 6 will end up in the player's hand.
        # Card 3 will end up in the dealer's hand, so there is a show card available.

        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','6'), Card('S','7'), Card('S','5'), Card('H','2'), Card('H','3')])

        # Assign the created deck to the sim object
        bjs.switch_deck(sd)
        
        # Add cards to the player's hand in the sim
        bjs.draw_for_player(2)
        
        # Add show card to dealer's hand in the sim
        bjs.draw_for_dealer(1)
        
        # Play the hand
        info = ps.play(bjs.player_hand_info, bjs.draw_for_player, bjs.get_dealer_show)
       
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S 2H 3H'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.STAND
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 17
        act_val = info.Count
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
