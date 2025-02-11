from enigma.pluglead import PlugLead

class PlugBoard:
    """
    PlugBoard coordinates up to 10 PlugLead instances to simulate an Enigma machine plug board.
    Maintains mapped_char_set to improve time efficiency of character mapping checking.
    """

    def __init__(self):
        self.__plug_leads = []
        self.__mapped_char_set = set()

    def add(self, mapping):
        if len(self.__plug_leads) >= 10:
            raise ValueError("Plug board supports a maximum of 10 plug leads")

        plug_lead = PlugLead(mapping)
        if plug_lead.first in self.__mapped_char_set or plug_lead.second in self.__mapped_char_set:
            raise ValueError("Plug lead characters must be unique")

        self.__plug_leads.append(plug_lead)
        self.__mapped_char_set.add(plug_lead.first)
        self.__mapped_char_set.add(plug_lead.second)

    def encode(self, character):
        if character not in self.__mapped_char_set:
            return character

        for plug_lead in self.__plug_leads:
            encoded = plug_lead.encode(character)
            if encoded != character:
                return encoded