import unittest
from deck import Deck, Stacked_Deck
from card import Card

class Test_Stacked_Deck(unittest.TestCase):
    
    def test_draw_one(self):
        d = Stacked_Deck()
        
        # Populate the deck with a full 52 card deck in a different order than constructed by the parent.
        # Intent is to have enough cards that we would not likely get a random draw from the parent that matched
        # The expected draw from the stacked child.
        d.deck.append(Card('D','A',1))
        d.deck.append(Card('D','2',2))
        d.deck.append(Card('D','3',3))
        d.deck.append(Card('D','4',4))
        d.deck.append(Card('D','5',5))
        d.deck.append(Card('D','6',6))
        d.deck.append(Card('D','7',7))
        d.deck.append(Card('D','8',8))
        d.deck.append(Card('D','9',9))
        d.deck.append(Card('D','10',10))
        d.deck.append(Card('D','J',10))
        d.deck.append(Card('D','Q',10))
        d.deck.append(Card('D','K',10))
        d.deck.append(Card('H','A',1))
        d.deck.append(Card('H','2',2))
        d.deck.append(Card('H','3',3))
        d.deck.append(Card('H','4',4))
        d.deck.append(Card('H','5',5))
        d.deck.append(Card('H','6',6))
        d.deck.append(Card('H','7',7))
        d.deck.append(Card('H','8',8))
        d.deck.append(Card('H','9',9))
        d.deck.append(Card('H','10',10))
        d.deck.append(Card('H','J',10))
        d.deck.append(Card('H','Q',10))
        d.deck.append(Card('H','K',10))
        d.deck.append(Card('C','A',1))
        d.deck.append(Card('C','2',2))
        d.deck.append(Card('C','3',3))
        d.deck.append(Card('C','4',4))
        d.deck.append(Card('C','5',5))
        d.deck.append(Card('C','6',6))
        d.deck.append(Card('C','7',7))
        d.deck.append(Card('C','8',8))
        d.deck.append(Card('C','9',9))
        d.deck.append(Card('C','10',10))
        d.deck.append(Card('C','J',10))
        d.deck.append(Card('C','Q',10))
        d.deck.append(Card('C','K',10)) 
        d.deck.append(Card('S','A',1))
        d.deck.append(Card('S','2',2))
        d.deck.append(Card('S','3',3))
        d.deck.append(Card('S','4',4))
        d.deck.append(Card('S','5',5))
        d.deck.append(Card('S','6',6))
        d.deck.append(Card('S','7',7))
        d.deck.append(Card('S','8',8))
        d.deck.append(Card('S','9',9))
        d.deck.append(Card('S','10',10))
        d.deck.append(Card('S','J',10))
        d.deck.append(Card('S','Q',10))
        d.deck.append(Card('S','K',10))
           
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
        c = Card('D', 'A', 1)
        exp_val = (c.suit, c.pips)
        act_val = (dc.suit, dc.pips)
        self.assertTupleEqual(exp_val, act_val)
        # Is the drawn card gone from the deck?
        self.assertTrue(dc not in d.deck)


if __name__ == '__main__':
    unittest.main()
