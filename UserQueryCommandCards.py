# Standard

# Local
from card import Card
from UserQueryCommand import UserQueryCommand


class UserQueryCommandCards(UserQueryCommand):
    """
    Following the Command design pattern, this is the ConcreateUserQueryCommand class that knows how to exeucte a Cards command.
    """
    def __init__(self, receiver=None, query_preface = ''):
        """
        :parameter receiver: The object that knows how to perform the operations associated with carrying out a command.
        :parameter query_preface: Text displayed to the user to request their response, string
        """
        UserQueryCommand.__init__(self, receiver)
        self._query_preface = query_preface
        
    def Execute(self):
        """
        Execution of Cards command obtains from the user a string like 'AS, 2H, KC 10D' that can be processed into a list of Cards and returns
        a list of Card objects
        :return: List of Card objects created from the user provided string   
        """

        processed_response = None
        
        prompt_text = self._query_preface + '\n'

        # Add to the prompt, giving the user examples of an acceptable response       
        prompt_text += '(examples AS KH QD JC 10S 9H 8D ... 2C): '
        
        while processed_response is None:
                
            # Ask the receiver/user for a raw response, which will be in the form of a string
            raw_response = self._receiver.GetRawResponse(prompt_text)
        
            # Process the response from the receiver/user into a Pitch
            try:
                processed_response = Card().make_card_list_from_str(raw_response)
            except:
                # Let the receiver/user know they provided an invalid response
                msg = '\n' + '\'' + raw_response + '\'' + ' is not a valid list of cards. Please try again.' 
                self._receiver.IssueErrorMessage(msg)
                
        return processed_response



