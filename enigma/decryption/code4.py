import itertools

from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard

def get_plug_board():
    plug_board = PlugBoard()
    plug_board.add("WP")
    plug_board.add("RJ")
    plug_board.add("VF")
    plug_board.add("HN")
    plug_board.add("CG")
    plug_board.add("BS")
    return plug_board

def get_enigma(plug_board):
    rotors = [
        {"name": "IV", "position": "U", "ring": 10},
        {"name": "III", "position": "W", "ring": 12},
        {"name": "V", "position": "S", "ring": 24}]
    return Enigma(plug_board, rotors, "A")

def decrypt(crib, message):
    valid_characters = ["D", "E", "K", "L", "M", "O", "Q", "T", "U", "X", "Y", "Z"]
    character_combinations = [x for x in itertools.permutations(valid_characters, 2)]
    for character_combination in character_combinations:
        plug_board = get_plug_board()
        plug_board.add("A" + character_combination[0])
        plug_board.add("I" + character_combination[1])
        enigma = get_enigma(plug_board)
        result = enigma.encrypt(message)
        if result.find(crib) > -1:
            print(f"Found result '{result}'")
            print(f"Found character combination '{character_combination}'\n")

if __name__ == '__main__':
    decrypt("TUTOR", "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW")
