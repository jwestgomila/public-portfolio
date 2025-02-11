from enigma.rotorconfiguration import RotorConfiguration, get_custom_reflector


class RotorAssembly:

    """
    RotorAssembly simulates the combined rotor mechanism of the real Enigma machine.
    It coordinates encryption, the reflector and rotor turnover.
    It also has the ability to take a custom, non-standard reflector as a parameter.

    rotor_settings are a rotor names, positions and ring settings.
    reflector is the reflector name .
    """
    def __init__(self, rotor_settings, reflector):
        rotor_configuration = RotorConfiguration()
        rotors = []
        for rotor_setting in rotor_settings:
            rotor = rotor_configuration.get_configuration(rotor_setting["name"], rotor_setting["position"], rotor_setting["ring"])
            rotors.append(rotor)
        self.rotors = rotors

        if isinstance(reflector, list):
            self.reflector = get_custom_reflector(reflector)
        else:
            self.reflector = rotor_configuration.get_configuration(reflector, None, None)

    def encrypt(self, letter):
        self.__turnover()
        return self.__encryption_cycle(letter)

    def __encryption_cycle(self, letter):
        for rotor in self.rotors:
            letter = rotor.encrypt_right_to_left(letter)

        letter = self.reflector.encrypt_left_to_right(letter)

        for i in range(len(self.rotors) - 1, -1, -1):
            rotor = self.rotors[i]
            letter = rotor.encrypt_left_to_right(letter)

        return letter

    def __turnover(self):
        should_turn_rotor_1 = self.rotors[0].turnover()
        if should_turn_rotor_1 or self.rotors[1].can_turnover():
            if self.rotors[1].turnover():
                self.rotors[2].turnover()
