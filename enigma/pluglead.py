class PlugLead:
    """
    PlugLead simulates the mapping between two characters in the Enigma machine PlugBoard.
    """

    def __init__(self, mapping):
        if len(mapping) != 2:
            raise ValueError("Plug lead character mapping must be of length 2")
        elif mapping[0] == mapping[1]:
            raise ValueError("Plug lead characters must be unique")

        self.first = mapping[0]
        self.second = mapping[1]

    def encode(self, character):
        """
        Encodes a character by returning its mapped character.
        If a mapping can't be found, return the original character (required according to problem specification
            even though it doesn't match actual plug lead mechanism).
        """
        if len(character) != 1:
            raise ValueError("Plug lead character must be a single character")

        if character == self.first:
            return self.second
        elif character == self.second:
            return self.first
        else:
            return character