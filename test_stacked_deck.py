import unittest
from deck import Deck, Stacked_Deck
from card import Card

class Test_Stacked_Deck(unittest.TestCase):
    
    def test_draw_one(self):
        d = Stacked_Deck()
        
        # Populate the deck with a full 52 card deck in a different order than constructed by the parent.
        # Intent is to have enough cards that we would not likely get a random draw from the parent that matched
        # The expected draw from the stacked child.
        
        d.add_card(Card('D','A'))
        d.add_card(Card('D','2'))
        d.add_card(Card('D','3'))
        d.add_card(Card('D','4'))
        d.add_card(Card('D','5'))
        d.add_card(Card('D','6'))
        d.add_card(Card('D','7'))
        d.add_card(Card('D','8'))
        d.add_card(Card('D','9'))
        d.add_card(Card('D','10'))
        d.add_card(Card('D','J'))
        d.add_card(Card('D','Q'))
        d.add_card(Card('D','K'))
        d.add_card(Card('H','A'))
        d.add_card(Card('H','2'))
        d.add_card(Card('H','3'))
        d.add_card(Card('H','4'))
        d.add_card(Card('H','5'))
        d.add_card(Card('H','6'))
        d.add_card(Card('H','7'))
        d.add_card(Card('H','8'))
        d.add_card(Card('H','9'))
        d.add_card(Card('H','10'))
        d.add_card(Card('H','J'))
        d.add_card(Card('H','Q'))
        d.add_card(Card('H','K'))
        d.add_card(Card('C','A'))
        d.add_card(Card('C','2'))
        d.add_card(Card('C','3'))
        d.add_card(Card('C','4'))
        d.add_card(Card('C','5'))
        d.add_card(Card('C','6'))
        d.add_card(Card('C','7'))
        d.add_card(Card('C','8'))
        d.add_card(Card('C','9'))
        d.add_card(Card('C','10'))
        d.add_card(Card('C','J'))
        d.add_card(Card('C','Q'))
        d.add_card(Card('C','K')) 
        d.add_card(Card('S','A'))
        d.add_card(Card('S','2'))
        d.add_card(Card('S','3'))
        d.add_card(Card('S','4'))
        d.add_card(Card('S','5'))
        d.add_card(Card('S','6'))
        d.add_card(Card('S','7'))
        d.add_card(Card('S','8'))
        d.add_card(Card('S','9'))
        d.add_card(Card('S','10'))
        d.add_card(Card('S','J'))
        d.add_card(Card('S','Q'))
        d.add_card(Card('S','K'))
           
        # Does the deck have the expected number of cards?
        exp_val = 52
        act_val = d.cards_remaining()
        self.assertEqual(exp_val, act_val)
        
        # Draw a card from the deck
        dc = d.draw()
        # Has the number of cards decreased by 1?
        exp_val = 51
        act_val = d.cards_remaining()
        self.assertEqual(exp_val, act_val)
        # Has the expected card been drawn?
        c = Card('D', 'A')
        exp_val = (c.get_suit(), c.get_pips())
        act_val = (dc.get_suit(), dc.get_pips())
        self.assertTupleEqual(exp_val, act_val)
        # Is the drawn card gone from the deck?
        self.assertTrue(dc not in d.deck)


if __name__ == '__main__':
    unittest.main()
