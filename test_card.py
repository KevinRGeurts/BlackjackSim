import unittest
from card import Card

class Test_Card(unittest.TestCase):
    def test_count_card_default(self):
        exp_val = 10
        c = Card()
        act_val = c.count_card()
        self.assertEqual(exp_val, act_val)
        
    def test_count_card_not_default(self):
        exp_val = 5
        c = Card(pips='5', count=5)
        act_val = c.count_card()
        self.assertEqual(exp_val, act_val)

    def test_count_card_ace_high(self):
        exp_val = 11
        c = Card(pips='A', count=1)
        act_val = c.count_card(True)
        self.assertEqual(exp_val, act_val)
        
    def test_count_card_ace_low(self):
        exp_val = 1
        c = Card(pips='A', count=1)
        act_val = c.count_card()
        self.assertEqual(exp_val, act_val)
        
    def test_print_card(self):
        exp_val = '7D' #Seven of diamonds
        c = Card(suit='D', pips='7', count=7)
        act_val = c.print_card()
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
    
