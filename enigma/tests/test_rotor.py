import unittest

from enigma.rotorconfiguration import RotorConfiguration


class TestRotor(unittest.TestCase):

    def test_encrypt_right_to_left(self):
        rotor = RotorConfiguration().get_configuration("I", "A", 1)
        self.assertEqual(rotor.encrypt_right_to_left("A"), "E")

    def test_encrypt_right_to_left_position(self):
        rotor = RotorConfiguration().get_configuration("I", "D", 1)
        self.assertEqual(rotor.encrypt_right_to_left("A"), "C")

    def test_encrypt_right_to_left_ring(self):
        rotor = RotorConfiguration().get_configuration("I", "A", 4)
        self.assertEqual(rotor.encrypt_right_to_left("A"), "U")

    def test_encrypt_left_to_right(self):
        rotor = RotorConfiguration().get_configuration("I", "A", 1)
        self.assertEqual(rotor.encrypt_left_to_right("A"), "U")

    def test_encrypt_left_to_right_position(self):
        rotor = RotorConfiguration().get_configuration("I", "B", 1)
        self.assertEqual(rotor.encrypt_left_to_right("A"), "V")

    def test_encrypt_left_to_right_position_version_2(self):
        rotor = RotorConfiguration().get_configuration("I", "D", 1)
        self.assertEqual(rotor.encrypt_left_to_right("A"), "D")

    def test_encrypt_left_to_right_ring(self):
        rotor = RotorConfiguration().get_configuration("I", "A", 4)
        self.assertEqual(rotor.encrypt_left_to_right("U"), "A")
