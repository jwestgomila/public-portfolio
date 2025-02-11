import unittest

from enigma.rotorassembly import RotorAssembly


class TestRotorAssembly(unittest.TestCase):

    def test_encrypt_IV_III_I(self):
        test_rotors = [
            {"name": "IV", "position": "Z", "ring": 19},
            {"name": "III", "position": "V", "ring": 15},
            {"name": "I", "position": "A", "ring": 1}]
        test_assembly = RotorAssembly(test_rotors, "B")
        self.assertEqual(test_assembly.encrypt("A"), "R")

    def test_encrypt_III_II_I(self):
        test_rotors = [
            {"name": "III", "position": "A", "ring": 6},
            {"name": "II", "position": "A", "ring": 10},
            {"name": "I", "position": "A", "ring": 24}]
        test_assembly = RotorAssembly(test_rotors, "B")
        self.assertEqual(test_assembly.encrypt("A"), "R")

    def test_encrypt_III_V_IV(self):
        test_rotors = [
            {"name": "III", "position": "A", "ring": 24},
            {"name": "V", "position": "A", "ring": 9},
            {"name": "IV", "position": "A", "ring": 14}]
        test_assembly = RotorAssembly(test_rotors, "B")
        self.assertEqual(test_assembly.encrypt("A"), "B")
