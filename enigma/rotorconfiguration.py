import json
import os

from enigma.rotor import Rotor


def get_custom_reflector(alphabet):
    return Rotor("custom_reflector", alphabet, None, None, None)

class RotorConfiguration:
    def __init__(self):
        self.__rotor_configuration_path = RotorConfiguration.__get_relative_path("data/rotorconfiguration.json")
        self.__rotor_configuration = RotorConfiguration.__read_file(self.__rotor_configuration_path)

    def get_configuration(self, rotor, position_setting, ring_setting):
        if not rotor in self.__rotor_configuration:
            raise ValueError(f"Rotor '{rotor}' not found in rotor configuration")

        configured_rotor = self.__rotor_configuration[rotor]
        return Rotor(rotor, configured_rotor['alphabet'], configured_rotor['notch_setting'], position_setting, ring_setting)

    @staticmethod
    def __get_relative_path(path_in_project):
        project_directory = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(project_directory, path_in_project)

    @staticmethod
    def __read_file(filename):
        try:
            with open(filename) as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Cannot find rotor configuration data file at path '{filename}'")
        except json.decoder.JSONDecodeError as e:
            raise json.decoder.JSONDecodeError(f"Failed to deserialize rotor configuration file at path '{filename}'", e.doc, e.pos)
