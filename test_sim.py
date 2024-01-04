import unittest
from BlackJackSim import BlackJackSim
from deck import Stacked_Deck
from card import Card

class Test_Sim(unittest.TestCase):

    # TODO: Need many more test cases of play_dealer_hand to fully test the possibilities of the while looping and conditional branches

    def test_play_dealer_hand(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A',1), Card('D','J',10)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5',5), Card('H','2',2)])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
        # Do we have the expected final hand?
        exp_val = '5S 2H AC'
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


    def test_play_player_hand(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A',1), Card('D','J',10)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        # Set up player hand
        bjs.player_hand.add_cards([Card('S','5',5), Card('H','2',2)])
        
        # Play the dealer hand
        info = bjs.play_player_hand()
        
        # Do we have the expected final hand?
        exp_val = '5S 2H AC'
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


if __name__ == '__main__':
    unittest.main()
