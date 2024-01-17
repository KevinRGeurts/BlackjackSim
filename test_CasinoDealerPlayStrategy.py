import unittest
from PlayStrategy import BlackJackPlayStatus, CasinoDealerPlayStrategy
from hand import Hand
from deck import Stacked_Deck
from card import Card

class Test_CasinoDealerPlayStrategy(unittest.TestCase):
    
    def test_play_stand_min(self):
        
        ps = CasinoDealerPlayStrategy()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','2')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','8'), Card('D','J')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = '8C JD'
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


    def test_play_stand_max(self):
        
        ps = CasinoDealerPlayStrategy()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('S','5'), Card('H','2')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('C','A'), Card('D','J')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = 'AC JD'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.STAND
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 21
        act_val = info.Count
        self.assertEqual(exp_val, act_val)
       
    
    def test_play_hit_to_stand_max(self):
        
        ps = CasinoDealerPlayStrategy()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A'), Card('D','J')]
        
        # Set up the hand
        h = Hand()
        h.add_cards([Card('S','5'), Card('H','2')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = '5S 2H AC'
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

   
    def test_play_hit_to_bust_max_stand_min(self):
        
        ps = CasinoDealerPlayStrategy()
       
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A'), Card('D','J')]
       
        # Set up hand
        h = Hand()
        h.add_cards([Card('S','7'), Card('H','9')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = '7S 9H AC'
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
        

    def test_play_hit_to_bust_max_hit_to_stand_min(self):
        
        ps = CasinoDealerPlayStrategy()
       
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A'), Card('D','3')]
       
        # Set up hand
        h = Hand()
        h.add_cards([Card('S','7'), Card('H','8')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = '7S 8H AC 3D'
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
        
    
    def test_play_hit_to_bust_max_hit_to_bust_min(self):
        
        ps = CasinoDealerPlayStrategy()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A'), Card('D','J')]
       
        # Set up hand
        h = Hand()
        h.add_cards([Card('S','7'), Card('H','8')])
        
        # Play the hand
        info = ps.play(h, sd)
        
        # Do we have the expected final hand?
        exp_val = '7S 8H AC JD'
        act_val = info.Final_Hand
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = BlackJackPlayStatus.BUST
        act_val = info.Status
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 26
        act_val = info.Count
        self.assertEqual(exp_val, act_val)

 
if __name__ == '__main__':
    unittest.main()
