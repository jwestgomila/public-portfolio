import unittest

from enigma.pluglead import PlugLead


class TestPlugLead(unittest.TestCase):

    def test_init_len_check(self):
        self.assertRaises(ValueError, lambda: PlugLead("A"))

    def test_init_char_equiv_check(self):
        self.assertRaises(ValueError, lambda: PlugLead("AA"))

    def test_multi_encode_check(self):
        plug_lead = PlugLead("AB")
        self.assertRaises(ValueError, lambda: plug_lead.encode("AA"))

    def test_encode_first(self):
        plug_lead = PlugLead("AB")
        self.assertEqual(plug_lead.encode("A"), "B")

    def test_encode_second(self):
        plug_lead = PlugLead("AB")
        self.assertEqual(plug_lead.encode("B"), "A")

    def test_encode_none(self):
        plug_lead = PlugLead("AB")
        self.assertEqual(plug_lead.encode("C"), "C")
