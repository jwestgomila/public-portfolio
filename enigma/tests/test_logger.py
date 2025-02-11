import logging
import unittest
from unittest.mock import patch

from enigma.logger import Logger


class TestLogger(unittest.TestCase):

    @patch('logging.Logger.debug')
    def test_debug_method(self, mock_debug):
        test_message = "Test message"
        Logger.debug(test_message)
        mock_debug.assert_called_once_with(test_message)

    @patch('logging.basicConfig')
    def test_logger_initialization(self, mock_basic_config):
        Logger.set_default_handler()
        mock_basic_config.assert_called_once_with(filename="enigma.log", level=logging.DEBUG)
