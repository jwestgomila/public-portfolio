import logging

class Logger:
    """
    Logger is a static module level logging service.
    At present, only exposes debug logging interface, but can be freely extended.
    """

    logger = logging.getLogger("enigma")

    @staticmethod
    def set_default_handler():
        """
        Separate handler initialisation to avoid IO during tests.
        """
        if not Logger.logger.handlers:
            logging.basicConfig(filename="enigma.log", level=logging.DEBUG)
        return Logger.logger

    @staticmethod
    def debug(message):
        Logger.logger.debug(message)