import unittest

from enigma.rotorconfiguration import RotorConfiguration

# Tested implicitly in test_rotor.py
class TestRotorConfiguration(unittest.TestCase):

    def test_get_rotor(self):
        rotor = RotorConfiguration().get_configuration("III", "A", 1)
        self.assertEqual(rotor.__dict__.__len__(), 5)
