# Standard
import unittest

# Local
from deck import ShoeDeck
from card import Card

class Test_ShoeDeck(unittest.TestCase):
        
    def test_shoe_creation(self):
        d = ShoeDeck(5)
        # Does shoe have the expected number of cards?
        self.assertEqual(5*52, d.cards_remaining())
    
    
    def test_draw_too_many_cards(self):
        from random import seed
        seed(1234567890)
        d = ShoeDeck(5)
        # Draw one more card than is available in the shoe, to force the shoe to be rebuilt to provide the last card of the draw
        dc = d.draw(5*52+1)
        # Deck should have 5*52-1 cards
        self.assertEqual(5*52-1, d.cards_remaining())
        # Has the expected card been drawn last?
        c = Card('H', '3')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc[len(dc)-1].get_suit(), dc[len(dc)-1].get_pips())
        self.assertTupleEqual(exp_val, act_val)
        

if __name__ == '__main__':
    unittest.main()
