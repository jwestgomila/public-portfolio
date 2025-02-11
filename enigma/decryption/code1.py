from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard


def decrypt(plug_board, rotors, crib, message):
    reflectors = ["A", "B", "C"]
    for reflector in reflectors:
        enigma = Enigma(plug_board, rotors, reflector)
        result = enigma.encrypt(message)
        print(f"Found result '{result}'")
        if result.find(crib) > -1:
            print(f"Found missing reflector setting '{reflector}'")
            return reflector

if __name__ == '__main__':
    plug_board = PlugBoard()
    plug_board.add("KI")
    plug_board.add("XN")
    plug_board.add("FL")

    rotors = [
        {"name": "V", "position": "M", "ring": 14},
        {"name": "Gamma", "position": "J", "ring": 2},
        {"name": "Beta", "position": "M", "ring": 4}]

    decrypt(plug_board, rotors, "SECRETS", "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ")
