import unittest

from enigma.plugboard import PlugBoard


class TestPlugBoard(unittest.TestCase):

    def test_max_size_check(self):
        plug_board = PlugBoard()
        for i in range(1, 20, 2):
            char_1 = chr(ord("A") + i - 1)
            char_2 = chr(ord("A") + i)
            plug_board.add(char_1 + char_2)

        self.assertRaises(ValueError, lambda: plug_board.add("YZ"))

    def test_unique_lead_check(self):
        plug_board = PlugBoard()
        plug_board.add("AB")
        self.assertRaises(ValueError, lambda: plug_board.add("AB"))

    def test_encode(self):
        plug_board = PlugBoard()
        plug_board.add("AB")
        plug_board.add("YZ")

        self.assertEqual(plug_board.encode("A"), "B")
        self.assertEqual(plug_board.encode("B"), "A")
        self.assertEqual(plug_board.encode("Y"), "Z")
        self.assertEqual(plug_board.encode("Z"), "Y")
