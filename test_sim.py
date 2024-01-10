import unittest
from BlackJackSim import BlackJackSim
from deck import Stacked_Deck
from card import Card

class Test_Sim(unittest.TestCase):

    def test_check_blackjack_neither(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5',5), Card('H','2',2)])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K',10), Card('D','Q',10)])
        
        info = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = 'play on'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
 
    def test_check_blackjack_dealer(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','A',1), Card('H','J',10)])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K',10), Card('D','Q',10)])
        
        info = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = 'dealer blackjack'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)        

    def test_check_blackjack_player(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5',5), Card('H','2',2)])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K',10), Card('D','A',1)])
        
        info = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = 'player blackjack'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)        

    def test_check_blackjack_both(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','10',10), Card('H','A',1)])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K',10), Card('D','A',1)])
        
        info = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = 'both blackjack'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)        

    
    def test_play_dealer_hand_hit_to_stand(self):
        
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

    
    def test_play_dealer_hand_hit_to_bust_max_stand_min(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A',1), Card('D','J',10)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','7',7), Card('H','9',9)])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
        # Do we have the expected final hand?
        exp_val = '7S 9H AC'
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

    
    def test_play_dealer_hand_hit_to_bust_max_hit_to_stand_min(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A',1), Card('D','3',3)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','7',7), Card('H','8',8)])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
        # Do we have the expected final hand?
        exp_val = '7S 8H AC 3D'
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

    def test_play_dealer_hand_hit_to_bust_max_hit_to_bust_min(self):
        
        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A',1), Card('D','J',10)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','7',7), Card('H','8',8)])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
        # Do we have the expected final hand?
        exp_val = '7S 8H AC JD'
        act_val = info['Final_Hand']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected status?
        exp_val = 'bust'
        act_val = info['Status']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected final count?
        exp_val = 26
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
        
    
    def test_play_game_dealer_blackjack(self):

        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
        sd.deck = [Card('C','A',1), Card('D','J',10), Card('S','5',5), Card('H','2',2)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        info = bjs.play_game()
 
        # Do we have the expected game outcome?
        exp_val = 'dealer wins'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info['Dealer_Final_Hand']
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info['Player_Final_Hand']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected statuses?
        exp_val = 'blackjack'
        act_val = info['Dealer_Status']
        self.assertEqual(exp_val, act_val)
        
        exp_val = 'none'
        act_val = info['Player_Status']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info['Dealer_Count']
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info['Player_Count']
        self.assertEqual(exp_val, act_val)

    
    def test_play_game_player_blackjack(self):

        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
        sd.deck = [Card('S','5',5), Card('H','2',2), Card('C','A',1), Card('D','J',10)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        info = bjs.play_game()
 
        # Do we have the expected game outcome?
        exp_val = 'player wins'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info['Player_Final_Hand']
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info['Dealer_Final_Hand']
        self.assertEqual(exp_val, act_val)
     
        # Do we have the expected statuses?
        exp_val = 'blackjack'
        act_val = info['Player_Status']
        self.assertEqual(exp_val, act_val)
        
        exp_val = 'none'
        act_val = info['Dealer_Status']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info['Player_Count']
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info['Dealer_Count']
        self.assertEqual(exp_val, act_val)


    def test_play_game_both_blackjack(self):

        bjs = BlackJackSim()
        info = {}
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
        sd.deck = [Card('S','10',10), Card('H','A',1), Card('C','A',1), Card('D','J',10)]
        # Replace sim's deck with the Stacked_Deck
        bjs.deck = sd
       
        info = bjs.play_game()
 
        # Do we have the expected game outcome?
        exp_val = 'push'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info['Player_Final_Hand']
        self.assertEqual(exp_val, act_val)
       
        exp_val = '10S AH'
        act_val = info['Dealer_Final_Hand']
        self.assertEqual(exp_val, act_val)
     
        # Do we have the expected statuses?
        exp_val = 'blackjack'
        act_val = info['Player_Status']
        self.assertEqual(exp_val, act_val)
        
        exp_val = 'blackjack'
        act_val = info['Dealer_Status']
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info['Player_Count']
        self.assertEqual(exp_val, act_val)
        
        exp_val = 21
        act_val = info['Dealer_Count']
        self.assertEqual(exp_val, act_val)
        
    
    def test_determine_game_outcome(self):
        
        sim = BlackJackSim()
        
        info = {}

        # Test dealer busts...

        info['Player_Status'] = 'stand'
        info['Player_Count'] = 0
        info['Dealer_Status'] = 'bust'
        info['Dealer_Count'] = 0
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game outcome?
        exp_val = 'player wins'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)
 
        # Test player busts...

        info['Player_Status'] = 'bust'
        info['Player_Count'] = 0
        info['Dealer_Status'] = 'stand'
        info['Dealer_Count'] = 0
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game outcome?
        exp_val = 'dealer wins'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)
        
        # Test both stand, player has high score...
        info['Player_Status'] = 'stand'
        info['Player_Count'] = 19
        info['Dealer_Status'] = 'stand'
        info['Dealer_Count'] = 17
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game outcome?
        exp_val = 'player wins'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)

        # Test both stand, dealer has high score...
        info['Player_Status'] = 'stand'
        info['Player_Count'] = 19
        info['Dealer_Status'] = 'stand'
        info['Dealer_Count'] = 20
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game outcome?
        exp_val = 'dealer wins'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)

        # Test both stand, tie score...
        info['Player_Status'] = 'stand'
        info['Player_Count'] = 19
        info['Dealer_Status'] = 'stand'
        info['Dealer_Count'] = 19
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game outcome?
        exp_val = 'push'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)
        
        # Test both bust, it's a push...
        info['Player_Status'] = 'bust'
        info['Player_Count'] = 0
        info['Dealer_Status'] = 'bust'
        info['Dealer_Count'] = 0
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game outcome?
        exp_val = 'push'
        act_val = info['Game_Outcome']
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
