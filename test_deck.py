import unittest
from deck import Deck
from card import Card

class Test_Deck(unittest.TestCase):
    
    def test_cards_remaining(self):
        exp_val = 52
        d = Deck()
        act_val = d.cards_remaining()
        self.assertEqual(exp_val, act_val)
        
    def test_draw_one_not_infinite(self):
        from random import seed
        seed(1234567890)
        d = Deck()
        dc = d.draw()
        # Has the number of cards decreased by 1?
        self.assertEqual(51, d.cards_remaining())
        # Has the expected card been drawn?
        c = Card('H', 'Q')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc.get_suit(), dc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
        # Is the drawn card gone from the deck?
        self.assertTrue(dc not in d.deck)
        
    def test_draw_all_not_infinite(self):
        from random import seed
        seed(1234567890)
        d = Deck()
        dc = d.draw(52)
        # Are there no cards remaining in the deck?
        self.assertEqual(0, d.cards_remaining())
        # Is there 52 cards in the draw?
        self.assertEqual(52, len(dc))
        
    def test_draw_one_infinite(self):
        from random import seed
        seed(1234567890)
        # Create an "infinte" deck
        d = Deck(True)
        dc = d.draw()
        # Has the number of cards remained 52?
        self.assertEqual(52, d.cards_remaining())
        # Has the expected card been drawn?
        c = Card('H', 'Q')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc.get_suit(), dc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
        # Is the drawn card still in the deck?
        self.assertTrue(dc in d.deck)
        
    def test_draw_too_many_cards(self):
        # TODO: Fix this test which always fails. Probably something wrong with my understanding of asserts/exceptions in Python.
        from random import seed
        seed(1234567890)
        d = Deck()
        # Note that the second argument to assertRaises(...) must be a callable, with its argument list then following.
        # Or it might be easier to use the second sytax that has the "with".
        self.assertRaises(AssertionError, d.draw, 53)
        # Alternatively, this syntax also works.
        #with self.assertRaises(AssertionError):
        #    d.draw(53)
        

if __name__ == '__main__':
    unittest.main()
