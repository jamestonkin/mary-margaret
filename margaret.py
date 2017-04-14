import sys
import pickle

class Margaret:

    """ Contains methods to write messages by Margaret via command line to a dictionary, where Margaret is the key, and the value is the most recent message in a list.
    """

    def __init__(self):
        """ Creates dictionary and list value.
        """
        self.dict = {}
        self.marge_messages = []
        try:
            self.dict = self.deserialize()
        except FileNotFoundError:
            pass

    def save_message(self):
        """ Saves message in dictionary with Margaret as key. Then runs serialize function.
        """
        self.marge_messages.append(sys.argv[1:])
        self.dict['Margaret'] = self.marge_messages
        self.serialize()

    def serialize(self):
        """ Writes message to file
        """
        with open('messages.txt', 'wb+') as f:
            pickle.dump(self.dict, f)

    def deserialize(self):
        """ Reads message from file
        """
        try:
            with open('messages.txt', 'rb+') as f:
                self.dict = pickle.load(f)
        except EOFError:
            pass

        return self.dict

        return self.mary_messages['Margaret']

if __name__ == '__main__':
    marge = Margaret()
    marge.save_message()
    marge.deserialize()
