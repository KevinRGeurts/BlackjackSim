import unittest
from hand import Hand
from card import Card

class Test_Hand(unittest.TestCase):
   

    def test_add_card(self):
        
        h = Hand()
        c = Card('S','J')
        h.add_cards(c)
    
        # Do we have the expected number, 1, of cards in the hand?
        exp_val = 1
        act_val = len(h.cards)
        self.assertEqual(exp_val, act_val)
        # Is the first card in the hand the card we expect?
        exp_val = (c.suit, c.pips)
        act_val = (h.cards[0].suit, h.cards[0].pips)
        self.assertTupleEqual(exp_val, act_val)
 

    def test_add_cards(self):
    
        h = Hand()
        cards=[Card('S','J'), Card('H','3')]
        h.add_cards(cards)
    
        # Do we have the expected number, 2, of cards in the hand?
        exp_val = 2
        act_val = len(h.cards)
        self.assertEqual(exp_val, act_val)
        # Is the first card in the hand the card we expect?
        exp_val = (cards[0].suit, cards[0].pips)
        act_val = (h.cards[0].suit, h.cards[0].pips)
        self.assertTupleEqual(exp_val, act_val)
        # Is the second card in the hand the card we expect?
        exp_val = (cards[1].suit, cards[1].pips)
        act_val = (h.cards[1].suit, h.cards[1].pips)
        self.assertTupleEqual(exp_val, act_val)
    
    def test_get_num_aces(self):
        
        h1 = Hand()
        cards=[Card('S','J'), Card('H','3'), Card("D","A"),  Card("C","A")]
        h1.add_cards(cards)
        
        h2 = h1.get_aces()
    
        # Do we have the expected number, 2, of ace cards in the hand?
        exp_val = 2
        act_val = h2.get_num_aces()
        self.assertEqual(exp_val, act_val)

     
    def test_get_num_non_aces(self):
        
        h1 = Hand()
        cards=[Card('S','J'), Card('H','3'), Card("D","A"),  Card("C","A")]
        h1.add_cards(cards)
        
        h2 = h1.get_non_aces()
    
        # Do we have the expected number, 2, of ace cards in the hand?
        exp_val = 2
        act_val = h2.get_num_non_aces()
        self.assertEqual(exp_val, act_val)      
    
       
    def test_get_non_aces(self):
        
        h1 = Hand()
        cards=[Card('S','J'), Card('H','3'), Card("D","A"),  Card("C","A")]
        h1.add_cards(cards)
        
        h2 = h1.get_non_aces()
    
        # Do we have the expected number, 2, of non ace cards in the hand?
        exp_val = 2
        act_val = len(h2.cards)
        self.assertEqual(exp_val, act_val)
        # Is the first card in the new non aces hand the card we expect?
        exp_val = (cards[0].suit, cards[0].pips)
        act_val = (h2.cards[0].suit, h2.cards[0].pips)
        self.assertTupleEqual(exp_val, act_val)
        # Is the second card in the non aces hand the card we expect?
        exp_val = (cards[1].suit, cards[1].pips)
        act_val = (h2.cards[1].suit, h2.cards[1].pips)
        self.assertTupleEqual(exp_val, act_val)
       
   
    def test_get_aces(self):
        
        h1 = Hand()
        cards=[Card('S','J'), Card('H','3'), Card("D","A"),  Card("C","A")]
        h1.add_cards(cards)
        
        h2 = h1.get_aces()
    
        # Do we have the expected number, 2, of ace cards in the hand?
        exp_val = 2
        act_val = len(h2.cards)
        self.assertEqual(exp_val, act_val)
        # Is the first card in the new aces hand the card we expect?
        exp_val = (cards[2].suit, cards[2].pips)
        act_val = (h2.cards[0].suit, h2.cards[0].pips)
        self.assertTupleEqual(exp_val, act_val)
        # Is the second card in the new aces hand the card we expect?
        exp_val = (cards[3].suit, cards[3].pips)
        act_val = (h2.cards[1].suit, h2.cards[1].pips)
        self.assertTupleEqual(exp_val, act_val)

    
    def test_count_hand(self):
    
        h = Hand()
        cards=[Card('S','J'), Card('H','3'), Card("D","A")]
        h.add_cards(cards)
    
        exp_val = 14
        act_val = h.count_hand()
        self.assertEqual(exp_val, act_val)
        
    
    def test_hand_info(self):
        
        h = Hand()
        cards=[Card('S','J'), Card('H','3'), Card('S','5'), Card("D","A"),  Card("C","A")]
        h.add_cards(cards)
        
        info = h.hand_info()
        
        # Do we have the expected number, 2, of ace cards in the hand?
        exp_val = 2
        act_val = info['Num_Aces']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected number, 3 of non ace cards in the hand?
        exp_val = 3
        act_val = info['Num_Other']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected value of summed up pips of the cards in the hand that are not aces?
        exp_val = 18
        act_val = info['Count_Other']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected value of summed up pips of all cards in the hand, with any aces treated as "low"
        exp_val = 20
        act_val = info['Count_Min']
        self.assertEqual(exp_val, act_val)
        # Do we have the expected value of summed up pips of all cards in the hand, with the first ace if any treated as "high"
        # and any additional aces treated as "low"
        exp_val = 30
        act_val = info['Count_Max']
        self.assertEqual(exp_val, act_val)
        
    
    def test_print_hand(self):
        
        h = Hand()
        cards=[Card('S','J'), Card('H','3'), Card('S','5'), Card("D","A"),  Card("C","A")]
        h.add_cards(cards)
        
        exp_val = 'JS 3H 5S AD AC'
        act_val = h.print_hand()
        self.assertEqual(exp_val, act_val)
        

if __name__ == '__main__':
    unittest.main()


