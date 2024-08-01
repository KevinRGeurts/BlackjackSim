# Standard
import unittest
from unittest.mock import patch
import io

# Local
import UserQueryReceiver
from UserQueryCommandCards import UserQueryCommandCards
from hand import Hand


class Test_UserQueryCommandCards(unittest.TestCase):
    
    # Apply a patch() decorator to replace keyboard input from user with a string.
    # The patch should result in first an invalid response, and then a valid response.
    @patch('sys.stdin', io.StringIO('AX\nAS KH QD JC 10H 2S\n'))
    def test_cards_command(self):
        
        receiver = UserQueryReceiver.UserQueryReceiver_GetCommandReceiver()
        query_preface = 'Enter player deal up to two cards.'
        command = UserQueryCommandCards(receiver, query_preface)
        
        exp_val = 'AS KH QD JC 10H 2S'
        card_list = command.Execute()
        h = Hand()
        h.add_cards(card_list)
        act_val = str(h)
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
