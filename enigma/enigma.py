from enigma.logger import Logger
from enigma.rotorassembly import RotorAssembly


class Enigma:
    """
    Enigma encapsulates all the logic required to simulate an Enigma machine.
    It coordinates the plug board along with the rotor assembly.

    plug_board is the set of plug_board character mappings.
    rotors are the rotors to be used in the simulation, with the zeroth element corresponding to the rightmost position in the machine.
    reflector is the reflector to be used in the simulation.
    """

    def __init__(self, plug_board, rotors, reflector):
        self.plug_board = plug_board
        self.rotor_assembly = RotorAssembly(rotors, reflector)
        Logger.set_default_handler()

    def encrypt(self, message):
        Logger.debug(f"Encrypting message '{message}'")

        encrypted_message = ""
        for letter in message.upper():
            plug_board_encrypted_letter_1 = self.plug_board.encode(letter)
            Logger.debug(f"Plug board '{letter}' to '{plug_board_encrypted_letter_1}'")

            rotor_encrypted_letter = self.rotor_assembly.encrypt(plug_board_encrypted_letter_1)
            Logger.debug(f"Rotor '{plug_board_encrypted_letter_1}' to '{rotor_encrypted_letter}'")

            plug_board_encrypted_letter_2 = self.plug_board.encode(rotor_encrypted_letter)
            Logger.debug(f"Plug board '{rotor_encrypted_letter}' to '{plug_board_encrypted_letter_2}'\n")

            encrypted_message += plug_board_encrypted_letter_2

        Logger.debug(f"Encrypted message '{encrypted_message}'")
        return encrypted_message
