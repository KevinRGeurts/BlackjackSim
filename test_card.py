# Standard
import unittest

# Local
from card import Card
from hand import Hand

class Test_Card(unittest.TestCase):
    def test_construct_card_bad_suit(self):
        self.assertRaises(AssertionError, Card().__init__, 'Z')    
    
    def test_count_card_default(self):
        exp_val = 10
        c = Card()
        act_val = c.count_card()
        self.assertEqual(exp_val, act_val)
        
    def test_count_card_not_default(self):
        exp_val = 5
        c = Card(pips='5')
        act_val = c.count_card()
        self.assertEqual(exp_val, act_val)

    def test_count_card_ace_high(self):
        exp_val = 11
        c = Card(pips='A')
        act_val = c.count_card(True)
        self.assertEqual(exp_val, act_val)
        
    def test_count_card_ace_low(self):
        exp_val = 1
        c = Card(pips='A')
        act_val = c.count_card()
        self.assertEqual(exp_val, act_val)
        
    def test_str(self):
        exp_val = '7D' #Seven of diamonds
        c = Card(suit='D', pips='7')
        act_val = str(c)
        self.assertEqual(exp_val, act_val)
        
    
    def test_get_count_from_pips(self):
        
        # Test for ace
        exp_val = 1
        act_val = Card().get_count_from_pips('A')
        self.assertEqual(exp_val, act_val)
        
        # Test for king
        exp_val = 10
        act_val = Card().get_count_from_pips('K')
        self.assertEqual(exp_val, act_val)

        # Test for queen
        exp_val = 10
        act_val = Card().get_count_from_pips('Q')
        self.assertEqual(exp_val, act_val)

        # Test for jack
        exp_val = 10
        act_val = Card().get_count_from_pips('J')
        self.assertEqual(exp_val, act_val)
        
        # Test branch for 1-10
        exp_val = 6
        act_val = Card().get_count_from_pips('6')
        self.assertEqual(exp_val, act_val)
        
        # Test trap bad pips
        self.assertRaises(AssertionError, Card().get_count_from_pips, '11')

    
    def test_get_pips(self):
        exp_val = 'Q'
        act_val = Card('S','Q').get_pips()
        self.assertEqual(exp_val, act_val)
        

    def test_get_suit(self):
        exp_val = 'S'
        act_val = Card('S','Q').get_suit()
        self.assertEqual(exp_val, act_val)
        

    def test_make_card_list_from_str(self):
        exp_val = 'AS KH QD JC 10H 2S'
        card_list = Card().make_card_list_from_str('AS KH QD JC 10H 2S')
        h = Hand()
        h.add_cards(card_list)
        act_val = str(h)
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
    
