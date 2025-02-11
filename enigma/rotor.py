from enigma.logger import Logger


class Rotor:
    """
    Rotor simulates individual rotor type components in the Enigma machine, including reflectors.
    """

    __alphabet_size = 26
    __ord_a = ord('A')

    """
    name is the rotor name, used for user friendly logging.
    alphabet is a list containing 26 elements, each a letter in the range A to Z.
    notch_setting is a letter in the range A to Z and defines the position of the notch that drives rotor turnover.
    position_setting is a letter in the range A to Z and defines the starting position of the rotor.
    ring_setting is a number in the range 1 to 26 and is applied as a fixed offset to the configured rotor alphabet.
    """
    def __init__(self, name, alphabet, notch_setting, position_setting, ring_setting):
        self.__name = name
        self.__alphabet = alphabet
        self.__notch_setting = notch_setting

        if position_setting is None:
            self.__pointer = Rotor.__alphabet_size
        else:
            self.__pointer = Rotor.get_letter_position(position_setting) + Rotor.__alphabet_size

        if ring_setting is None: ring_setting = 1
        self.__ring_setting = ring_setting - 1

    def encrypt_right_to_left(self, letter):
        adjusted_letter_position = self.__get_adjusted_pointer(letter) % Rotor.__alphabet_size
        encrypted_letter = self.__alphabet[adjusted_letter_position]
        encrypted_letter_index = self.get_letter_position(encrypted_letter)
        adjusted_encrypted_letter = self.__get_adjusted_encrypted_letter(encrypted_letter_index)

        Logger.debug(f"Encrypted RTL letter '{letter}' to '{adjusted_encrypted_letter}'")
        return adjusted_encrypted_letter

    def encrypt_left_to_right(self, letter):
        adjusted_letter_position = self.__get_adjusted_pointer(letter) % Rotor.__alphabet_size
        adjusted_letter = chr(Rotor.__ord_a + adjusted_letter_position)
        encrypted_letter_index = self.__alphabet.index(adjusted_letter)
        encrypted_letter = self.__get_adjusted_encrypted_letter(encrypted_letter_index)

        Logger.debug(f"Encrypted LTR letter '{letter}' to '{encrypted_letter}'")
        return encrypted_letter

    def __get_adjusted_encrypted_letter(self, encrypted_letter_index):
        adjusted_encrypted_letter_position = (encrypted_letter_index + self.__ring_setting + Rotor.__alphabet_size - (self.__pointer % Rotor.__alphabet_size)) % Rotor.__alphabet_size
        return chr(Rotor.__ord_a + adjusted_encrypted_letter_position)

    def can_turnover(self):
        if self.__notch_setting is None:
            return False

        letter = self.get_position_letter()
        return True if letter == self.__notch_setting else False

    def turnover(self):
        letter = self.get_position_letter()
        self.__pointer += 1
        Logger.debug(f"Rotor '{self.__name}' turn '{letter}' to '{chr(self.__pointer % Rotor.__alphabet_size + Rotor.__ord_a)}'")

        if letter == self.__notch_setting:
            Logger.debug(f"Rotor '{self.__name}' trigger next turnover")
            return True
        return False

    def get_position_letter(self):
        return chr(self.__pointer % Rotor.__alphabet_size + Rotor.__ord_a)

    def get_alphabet(self):
        return self.__alphabet

    def __get_adjusted_pointer(self, letter):
        return self.__pointer - self.__ring_setting + Rotor.get_letter_position(letter)

    @staticmethod
    def get_letter_position(letter):
        return ord(letter) - Rotor.__ord_a
