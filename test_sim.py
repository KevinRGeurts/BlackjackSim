import unittest
from BlackJackSim import BlackJackSim, BlackJackCheck, BlackJackGameOutcome, GamePlayOutcome
from PlayStrategy import BlackJackPlayStatus
from deck import Stacked_Deck
from card import Card

class Test_Sim(unittest.TestCase):

    def test_get_dealer_show(self):
        bjs = BlackJackSim()
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5'), Card('H','2')])
        
        # Is the dealer's show card as expected?
        c = Card('S','5')
        sc = bjs.get_dealer_show()
        
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (sc.get_suit(), sc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
        
       
    def test_draw_for_dealer(self):
        bjs = BlackJackSim()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','J'), Card('S','4')])
        
        # Replace sim's deck with Stacked_Deck
        bjs.switch_deck(sd)

        # Draw a card
        dc = bjs.draw_for_dealer(1)
        dc = dc[0]
        
        # Did we get the one we expected?
        c = Card('C', 'A')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc.get_suit(), dc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
        

    def test_draw_for_player(self):
        bjs = BlackJackSim()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','J'), Card('S','4')])
        
        # Replace sim's deck with Stacked_Deck
        bjs.switch_deck(sd)

        # Draw a card
        dc = bjs.draw_for_player(1)
        dc = dc[0]
        
        # Did we get the one we expected?
        c = Card('C', 'A')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc.get_suit(), dc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
 
    
    def test_draw_for_split(self):
        bjs = BlackJackSim()
        
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','J'), Card('S','4')])
        
        # Replace sim's deck with Stacked_Deck
        bjs.switch_deck(sd)

        # Draw a card
        dc = bjs.draw_for_split(1)
        dc = dc[0]
        
        # Did we get the one we expected?
        c = Card('C', 'A')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc.get_suit(), dc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
    
    
    def test_check_blackjack_neither(self):
        
        bjs = BlackJackSim()
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5'), Card('H','2')])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K'), Card('D','Q')])
        
        act_val = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = BlackJackCheck.PLAY_ON
        self.assertEqual(exp_val, act_val)
 
    
    def test_check_blackjack_dealer(self):
        
        bjs = BlackJackSim()
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','A'), Card('H','J')])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K'), Card('D','Q')])
        
        act_val = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = BlackJackCheck.DEALER_BLACKJACK
        self.assertEqual(exp_val, act_val)        


    def test_check_blackjack_player(self):
        
        bjs = BlackJackSim()
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5'), Card('H','2')])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K'), Card('D','A')])
        
        act_val = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = BlackJackCheck.PLAYER_BLACKJACK
        self.assertEqual(exp_val, act_val)        


    def test_check_blackjack_both(self):
        
        bjs = BlackJackSim()
        
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','10'), Card('H','A')])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('C','K'), Card('D','A')])
        
        act_val = bjs.check_for_blackjack()
        
        # Do we have the expected status?
        exp_val = BlackJackCheck.BOTH_BLACKJACK
        self.assertEqual(exp_val, act_val)        

    
    def test_play_dealer_hand_hit_to_stand(self):
        
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.deck = [Card('C','A'), Card('D','J')]
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','5'), Card('H','2')])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
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
        

    def test_play_games_fixed_player_deal_and_dealer_show(self):
        from random import seed
        seed(1234567890)
        sim = BlackJackSim()
        player_deal=[Card('H','J'), Card('S','9')]
        dealer_show=Card('D','7')
        info = sim.play_games(100, player_deal, dealer_show)
        dw = info.Dealer_Wins
        pw = info.Player_Wins
        pu = info.Pushes
        dbj = info.Dealer_BlackJacks
        pbj = info.Player_BlackJacks
        # Do we have the expected dealer wins?
        exp_val = 7
        act_val = dw
        self.assertEqual(exp_val, act_val)
        # Do we have the expected player wins?
        exp_val = 79
        act_val = pw
        self.assertEqual(exp_val, act_val)
        # Do we have the expected pushes?
        exp_val = 14
        act_val = pu
        self.assertEqual(exp_val, act_val)
        # Do we have the expected dealer BlackJacks?
        exp_val = 0
        act_val = dbj
        self.assertEqual(exp_val, act_val)
        # Do we have the expected player BlackJacks?
        exp_val = 0
        act_val = pbj
        self.assertEqual(exp_val, act_val)
    
        
    def test_play_games(self):
        from random import seed
        seed(1234567890)
        sim = BlackJackSim()
        info = sim.play_games(100)
        dw = info.Dealer_Wins
        pw = info.Player_Wins
        pu = info.Pushes
        dbj = info.Dealer_BlackJacks
        pbj = info.Player_BlackJacks
        # Do we have the expected dealer wins?
        exp_val = 48
        act_val = dw
        self.assertEqual(exp_val, act_val)
        # Do we have the expected player wins?
        exp_val = 44
        act_val = pw
        self.assertEqual(exp_val, act_val)
        # Do we have the expected pushes?
        exp_val = 10
        act_val = pu
        self.assertEqual(exp_val, act_val)
        # Do we have the expected dealer BlackJacks?
        exp_val = 3
        act_val = dbj
        self.assertEqual(exp_val, act_val)
        # Do we have the expected player BlackJacks?
        exp_val = 5
        act_val = pbj
        self.assertEqual(exp_val, act_val)
        
        
    def test_play_game_with_dealer_show_specified(self):
            
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give the first card in deck to dealer, to supplement dealer_show
        sd.add_cards([Card('D','J'), Card('S','5'), Card('H','2')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        info = bjs.play_game(dealer_show=Card('C','A'))
 
        # Do we have the expected game outcome?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info.Dealer_Final_Hand
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected statuses?
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Dealer_Status
        self.assertEqual(exp_val, act_val)
        
        exp_val = BlackJackPlayStatus.NONE
        act_val = info.Player_Status
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info.Dealer_Count
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info.Player_Count
        self.assertEqual(exp_val, act_val)

    
    def test_play_game_with_dealer_show_and_player_deal_all_specified(self):
            
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give the first card in deck to dealer, to supplement dealer_show,
        # and no cards in deck to player to supplement player_deal.
        sd.add_cards([Card('D','J')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        info = bjs.play_game(player_deal=[Card('S','5'), Card('H','2')],dealer_show=Card('C','A'))
 
        # Do we have the expected game outcome?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info.Dealer_Final_Hand
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected statuses?
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Dealer_Status
        self.assertEqual(exp_val, act_val)
        
        exp_val = BlackJackPlayStatus.NONE
        act_val = info.Player_Status
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info.Dealer_Count
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info.Player_Count
        self.assertEqual(exp_val, act_val)

        
    def test_play_game_with_dealer_show_and_player_deal_part_specified(self):
            
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give the first card in deck to dealer, to supplement dealer_show,
        # and second card in deck to player to supplement player_deal.
        sd.add_cards([Card('D','J'), Card('H','2')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        info = bjs.play_game(player_deal=[Card('S','5')],dealer_show=Card('C','A'))
 
        # Do we have the expected game outcome?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info.Dealer_Final_Hand
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected statuses?
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Dealer_Status
        self.assertEqual(exp_val, act_val)
        
        exp_val = BlackJackPlayStatus.NONE
        act_val = info.Player_Status
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info.Dealer_Count
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info.Player_Count
        self.assertEqual(exp_val, act_val)
       
    
    def test_play_dealer_hand_hit_to_bust_max_stand_min(self):
        
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','J')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','7'), Card('H','9')])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
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

    
    def test_play_dealer_hand_hit_to_bust_max_hit_to_stand_min(self):
        
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','3')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','7'), Card('H','8')])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
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

    def test_play_dealer_hand_hit_to_bust_max_hit_to_bust_min(self):
        
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','J')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        # Set up dealer hand
        bjs.dealer_hand.add_cards([Card('S','7'), Card('H','8')])
        
        # Play the dealer hand
        info = bjs.play_dealer_hand()
        
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
    
    
    def test_play_player_hand(self):
        
        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        sd.add_cards([Card('C','A'), Card('D','J')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        # Set up dealer hand because play strategy may need a show Card
        bjs.dealer_hand.add_cards([Card('S','10'), Card('H','7')])
        
        # Set up player hand
        bjs.player_hand.add_cards([Card('S','5'), Card('H','2')])
        
        # Play the player's hand
        info = bjs.play_player_hand()
        
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
        
    
    def test_play_game_dealer_blackjack(self):

        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
        sd.add_cards([Card('C','A'), Card('D','J'), Card('S','5'), Card('H','2')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        info = bjs.play_game()
 
        # Do we have the expected game outcome?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info.Dealer_Final_Hand
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected statuses?
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Dealer_Status
        self.assertEqual(exp_val, act_val)
        
        exp_val = BlackJackPlayStatus.NONE
        act_val = info.Player_Status
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info.Dealer_Count
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info.Player_Count
        self.assertEqual(exp_val, act_val)

    
    def test_play_game_player_blackjack(self):

        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
        sd.add_cards([Card('S','5'), Card('H','2'), Card('C','A'), Card('D','J')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        info = bjs.play_game()
 
        # Do we have the expected game outcome?
        exp_val = BlackJackGameOutcome.PLAYER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)
       
        exp_val = '5S 2H'
        act_val = info.Dealer_Final_Hand
        self.assertEqual(exp_val, act_val)
     
        # Do we have the expected statuses?
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Player_Status
        self.assertEqual(exp_val, act_val)
        
        exp_val = BlackJackPlayStatus.NONE
        act_val = info.Dealer_Status
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info.Player_Count
        self.assertEqual(exp_val, act_val)
        
        exp_val = 0
        act_val = info.Dealer_Count
        self.assertEqual(exp_val, act_val)


    def test_play_game_both_blackjack(self):

        bjs = BlackJackSim()
        
        # Replace sim's deck with Stacked_Deck
        # Create a Stacked_Deck
        sd = Stacked_Deck()
        # It's assumed that BlackJackSim.play_game() will give first two cards in deck to dealer.
        sd.add_cards([Card('S','10'), Card('H','A'), Card('C','A'), Card('D','J')])
        # Replace sim's deck with the Stacked_Deck
        bjs.switch_deck(sd)
       
        info = bjs.play_game()
 
        # Do we have the expected game outcome?
        exp_val = BlackJackGameOutcome.PUSH
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final hands?
        exp_val = 'AC JD'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)
       
        exp_val = '10S AH'
        act_val = info.Dealer_Final_Hand
        self.assertEqual(exp_val, act_val)
     
        # Do we have the expected statuses?
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Player_Status
        self.assertEqual(exp_val, act_val)
        
        exp_val = BlackJackPlayStatus.BLACKJACK
        act_val = info.Dealer_Status
        self.assertEqual(exp_val, act_val)
        
        # Do we have the expected final counts?
        exp_val = 21
        act_val = info.Player_Count
        self.assertEqual(exp_val, act_val)
        
        exp_val = 21
        act_val = info.Dealer_Count
        self.assertEqual(exp_val, act_val)
        
    def test_game_with_split(self):
        
        sim = BlackJackSim()
        
        info = GamePlayOutcome()

        # Here is what will happen to the cards in the stacked deck
        # 1,2 dealt to dealer
        # 3,4 dealt to player before split
        # 5 dealt to player's split hand
        # 6 dealt to player's original hand after split
        sd = Stacked_Deck()
        sd.add_cards([Card('H','7'), Card('D','10'),Card('C','8'), Card('S','8'),Card('S','A'), Card('C','J')])
        sim.switch_deck(sd)
        
        # Play the game, which should result in a split
        info = sim.play_game()
        
        # Do we have the expected results for the first player hand
        exp_val = '8C JC'
        act_val = info.Player_Final_Hand
        self.assertEqual(exp_val, act_val)

        # Do we have the expected results for the second, split, player hand
        exp_val = '8S AS'
        act_val = info.Split_Final_Hand
        self.assertEqual(exp_val, act_val)
        
        
    
    def test_determine_game_outcome(self):
        
        sim = BlackJackSim()
        
        info = GamePlayOutcome()

        # Test dealer busts...
        
        info.Player_Status = BlackJackPlayStatus.STAND
        info.Player_Count = 0
        info.Dealer_Status = BlackJackPlayStatus.BUST
        info.Dealer_Count = 0
        info.Split_Status = BlackJackPlayStatus.STAND
        info.Split_Count = 0
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game and split game outcomes?
        exp_val = BlackJackGameOutcome.PLAYER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        act_val = info.Split_Game_Outcome
        self.assertEqual(exp_val, act_val)
 
        # Test player and split bust...

        info.Player_Status = BlackJackPlayStatus.BUST
        info.Player_Count = 0
        info.Dealer_Status = BlackJackPlayStatus.STAND
        info.Dealer_Count = 0
        info.Split_Status = BlackJackPlayStatus.BUST
        info.Split_Count = 0 
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game and split game outcomes?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        act_val = info.Split_Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Test all stand, player and split have high score...

        info.Player_Status = BlackJackPlayStatus.STAND
        info.Player_Count = 19
        info.Dealer_Status = BlackJackPlayStatus.STAND
        info.Dealer_Count = 17
        info.Split_Status = BlackJackPlayStatus.STAND
        info.Split_Count = 18
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game and split game outcomes?
        exp_val = BlackJackGameOutcome.PLAYER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        act_val = info.Split_Game_Outcome
        self.assertEqual(exp_val, act_val)

        # Test all stand, dealer has high score...

        info.Player_Status = BlackJackPlayStatus.STAND
        info.Player_Count = 19
        info.Dealer_Status = BlackJackPlayStatus.STAND
        info.Dealer_Count = 20
        info.Split_Status = BlackJackPlayStatus.STAND
        info.Player_Count = 18
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game and split game outcomes?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        act_val = info.Split_Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Test all stand, tie scores...

        info.Player_Status = BlackJackPlayStatus.STAND
        info.Player_Count = 19
        info.Dealer_Status = BlackJackPlayStatus.STAND
        info.Dealer_Count = 19
        info.Split_Status = BlackJackPlayStatus.STAND
        info.Split_Count = 19
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game and split game outcomes?
        exp_val = BlackJackGameOutcome.PUSH
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        act_val = info.Split_Game_Outcome
        self.assertEqual(exp_val, act_val)
        
        # Test all bust, it's wins by the dealer...

        info.Player_Status = BlackJackPlayStatus.BUST
        info.Player_Count = 0
        info.Dealer_Status = BlackJackPlayStatus.BUST
        info.Dealer_Count = 0
        info.Split_Status = BlackJackPlayStatus.BUST
        info.Split_Count = 0
        
        sim.determine_game_outcome(info)
            
        # Do we have the expected game and split game outcomes?
        exp_val = BlackJackGameOutcome.DEALER_WINS
        act_val = info.Game_Outcome
        self.assertEqual(exp_val, act_val)
        act_val = info.Split_Game_Outcome
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
