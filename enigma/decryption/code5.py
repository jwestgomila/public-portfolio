import itertools

from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard
from enigma.rotor import Rotor
from enigma.rotorconfiguration import RotorConfiguration

plug_board = PlugBoard()
plug_board.add("UG")
plug_board.add("IE")
plug_board.add("PO")
plug_board.add("NX")
plug_board.add("WT")

rotors = [
    {"name": "IV", "position": "L", "ring": 7},
    {"name": "II", "position": "J", "ring": 18},
    {"name": "V", "position": "A", "ring": 6}]

def build_pairs(reflector_alphabet):
    pairs = []
    visited = set()
    for i in range(len(reflector_alphabet)):
        letter = reflector_alphabet[i]
        letter_maps_to = chr(ord("A") + i)
        if letter in visited or letter_maps_to in visited:
            # Avoid equivalent pair orderings
            continue

        pairs.append((letter, letter_maps_to))
        visited.add(letter)
        visited.add(letter_maps_to)

    return pairs

def swap_reflector_pairs(reflector_alphabet, tuple_pair):
    reflector_alphabet[Rotor.get_letter_position(tuple_pair[0][0])] = tuple_pair[1][1]
    reflector_alphabet[Rotor.get_letter_position(tuple_pair[1][0])] = tuple_pair[0][1]
    reflector_alphabet[Rotor.get_letter_position(tuple_pair[1][1])] = tuple_pair[0][0]
    reflector_alphabet[Rotor.get_letter_position(tuple_pair[0][1])] = tuple_pair[1][0]

def check_crib(result, cribs):
    for crib in cribs:
        if result.find(crib) > -1:
            return crib
    return ""

def calculate_index_of_coincidence(decryption_result):
    freq_map = {char: decryption_result.count(char) for char in set(decryption_result) if char.isalpha()}
    numerator = 26 * sum(map(lambda x: x * (x - 1), freq_map.values()))
    denominator = len(decryption_result) * (len(decryption_result) - 1)
    return numerator / denominator

def decrypt(crib, message):
    reflector_names = ["A", "B", "C"]
    for reflector_name in reflector_names:
        reflector = RotorConfiguration().get_configuration(reflector_name, None, None)
        pairs = build_pairs(reflector.get_alphabet())
        quad_combinations = {x for x in itertools.combinations(pairs, 4)}

        for quad_combination in quad_combinations:
            pair_combinations = {x for x in itertools.combinations(quad_combination, 2)}
            visited_remaining_pair_combinations = set()

            for pair_combination in pair_combinations:
                if pair_combination in visited_remaining_pair_combinations:
                    # Avoid processing equivalent pair combinations, e.g. '(('R', 'B'), ('Q', 'E'))' and '(('Y', 'A'), ('P', 'I'))' vs
                    #     '(('Y', 'A'), ('P', 'I'))' and '(('R', 'B'), ('Q', 'E'))'
                    continue

                remaining_pair_combination = tuple(x for x in filter(lambda x: x not in pair_combination, quad_combination))
                visited_remaining_pair_combinations.add(remaining_pair_combination)

                reflector_alphabet = reflector.get_alphabet().copy()
                swap_reflector_pairs(reflector_alphabet, pair_combination)
                swap_reflector_pairs(reflector_alphabet, remaining_pair_combination)

                enigma = Enigma(plug_board, rotors, reflector_alphabet)
                result = enigma.encrypt(message)

                ioc = calculate_index_of_coincidence(result)
                if ioc > 1.6:
                    print(f"Found result '{result}' with high IoC '{ioc}'")

                actual_crib = check_crib(result, crib)
                if actual_crib != "":
                    print(f"Found result '{result}'")
                    print(f"Found crib '{actual_crib}'")
                    print(f"Found base reflector '{reflector_name}'")
                    print(f"Found reflector modifications '{pair_combination}' and '{remaining_pair_combination}'\n")

def validate_custom_reflector():
    custom_reflector_enigma = Enigma(plug_board, rotors, "B_MOD")
    custom_reflector_result = custom_reflector_enigma.encrypt("HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX")
    print(f"Custom reflector result '{custom_reflector_result}'")
    assert(custom_reflector_result == "YOUCANFOLLOWMYDOGONINSTAGRAMATTALESOFHOFFMANN")

if __name__ == '__main__':
    # validate_custom_reflector()
    decrypt(['INSTAGRAM'], "HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX")
