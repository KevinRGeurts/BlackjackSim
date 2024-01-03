import unittest
from hand import Hand
from card import Card

class Test_Hand(unittest.TestCase):
   
    if __name__ == '__main__':
        unittest.main()

    
    def test_add_cards(self):
    
        h = Hand()
        cards=[Card('S','J',10), Card('H','3',3)]
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
    
    
    def test_get_non_aces(self):
        
        h1 = Hand()
        cards=[Card('S','J',10), Card('H','3',3), Card("D","A",1),  Card("C","A",1)]
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
        cards=[Card('S','J',10), Card('H','3',3), Card("D","A",1),  Card("C","A",1)]
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
        cards=[Card('S','J',10), Card('H','3',3), Card("D","A",1)]
        h.add_cards(cards)
    
        exp_val = 14
        act_val = h.count_hand()
        self.assertEqual(exp_val, act_val)
        