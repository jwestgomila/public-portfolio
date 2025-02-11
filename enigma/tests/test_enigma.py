import unittest

from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard


class TestEnigma(unittest.TestCase):

    def test_enigma(self):
        plug_board = PlugBoard()
        plug_board.add("PC")
        plug_board.add("XZ")
        plug_board.add("FM")
        plug_board.add("QA")
        plug_board.add("ST")
        plug_board.add("NB")
        plug_board.add("HY")
        plug_board.add("OR")
        plug_board.add("EV")
        plug_board.add("IU")

        rotors = [
            {"name": "I", "position": "P", "ring": 5},
            {"name": "Beta", "position": "G", "ring": 3},
            {"name": "V", "position": "Z", "ring": 24},
            {"name": "IV", "position": "E", "ring": 18}]
        enigma = Enigma(plug_board, rotors, "A")
        encryption = enigma.encrypt("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI")

        self.assertEqual(encryption, "CONGRATULATIONSONPRODUCINGYOURWORKINGENIGMAMACHINESIMULATOR")