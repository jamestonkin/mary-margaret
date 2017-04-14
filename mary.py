import sys
import pickle

class Mary:

    """ Contains methods to write messages by Mary via command line to a dictionary, where Mary is the key, and the value is the most recent message in a list.
    """

    def __init__(self):
        """ Creates dictionary and list value.
        """
        self.dict = {}
        self.mary_messages = []
        try:
            self.dict = self.deserialize()
        except FileNotFoundError:
            pass

    def save_message(self):
        """ Saves message in dictionary with Mary as key. Then runs serialize function.
        """
        self.mary_messages.extend(sys.argv[1:])
        self.dict['Mary'] = self.mary_messages
        self.serialize()

    def serialize(self):
        """ Writes message to file
        """
        with open('messages.txt', 'wb+') as f:
            pickle.dump(self.dict, f)

    def deserialize(self):
        """ Reads message from file.
        """
        try:
            with open('messages.txt', 'rb+') as f:
                self.dict = pickle.load(f)
        except EOFError:
            pass

        return self.dict

        return self.mary_messages['Mary']

if __name__ == '__main__':
    mary = Mary()
    mary.save_message()
    mary.deserialize()
