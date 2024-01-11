import unittest
from PlayStrategy import HoylePlayerPlayStrategy
from hand import Hand
from deck import Stacked_Deck
from card import Card

class Test_HoylePlayerPlayStrategy(unittest.TestCase):
    # 	Check Count_Max
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
        
        ps = HoylePlayerPlayStrategy()
        info = {}
        
        # Create a Stacked_Deck (Doesn't matter what. Their should be no draws.)
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','2')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','A'), Card('D','7')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = 'AC 7D'
        act_val = info['Final_Hand']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = 'stand'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 18
        act_val = info['Count']
        self.assertEqual(exp_val, act_val)


    def test_play_bust_min(self):
        
        ps = HoylePlayerPlayStrategy()
        info = {}
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','K')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','A'), Card('D','6')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S KH'
        act_val = info['Final_Hand']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = 'bust'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 22
        act_val = info['Count']
        self.assertEqual(exp_val, act_val)

    
    def test_play_stand_min_over_seventeen(self):
        
        ps = HoylePlayerPlayStrategy()
        info = {}
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','7')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','A'), Card('D','6')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S 7H'
        act_val = info['Final_Hand']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = 'stand'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 19
        act_val = info['Count']
        self.assertEqual(exp_val, act_val)


    def test_play_stand_min_on_show_six_or_under(self):
        
        ps = HoylePlayerPlayStrategy()
        info = {}
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','2')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','A'), Card('D','6')])
        
        # Play the hand
        info = ps.play(h, sd, show = Card('S','6'))
        
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S 2H'
        act_val = info['Final_Hand']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = 'stand'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 14
        act_val = info['Count']
        self.assertEqual(exp_val, act_val)

 
    def test_play_stand_min_on_show_over_six(self):
        
        ps = HoylePlayerPlayStrategy()
        info = {}
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','2'), Card('H','3')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','A'), Card('D','6')])
        
        # Play the hand
        info = ps.play(h, sd, show = Card('S','7'))
        
        # Do we have the expected final hand?
        exp_val = 'AC 6D 5S 2H 3H'
        act_val = info['Final_Hand']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = 'stand'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 17
        act_val = info['Count']
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
