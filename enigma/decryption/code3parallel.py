import itertools
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Manager

from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard

crib = "THOUSANDS"
message = "ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY"

plug_board = PlugBoard()
plug_board.add("FH")
plug_board.add("TS")
plug_board.add("BE")
plug_board.add("UQ")
plug_board.add("KD")
plug_board.add("AL")

reflectors = ["A", "B", "C"]
rotor_names = ["II", "IV", "Beta", "Gamma"]
valid_ring_settings = [2, 4, 6, 8, 20, 22, 24, 26]
ring_settings = [x for x in itertools.product(valid_ring_settings, repeat=3)]
rotor_combinations = [x for x in itertools.permutations(rotor_names, 3)]

def get_rotors(rotors, rings):
    return [
        {"name": rotors[0], "position": "Y", "ring": rings[0]},
        {"name": rotors[1], "position": "M", "ring": rings[1]},
        {"name": rotors[2], "position": "E", "ring": rings[2]}]

def decrypt(reflector, event):
    for rotor_combination in rotor_combinations:
        for ring_setting in ring_settings:
            if event.is_set():
                return

            rotors = get_rotors(rotor_combination, ring_setting)
            enigma = Enigma(plug_board, rotors, reflector)
            result = enigma.encrypt(message)
            if result.find(crib) > -1:
                event.set()
                print(f"Found result '{result}'")
                print(f"Found rotors '{rotor_combination}'")
                print(f"Found ring settings '{ring_setting}'")
                print(f"Found reflector '{reflector}'")
                return True
    return False

if __name__ == '__main__':
    start = time.time()
    with Manager() as manager:
        event = manager.Event()
        with ProcessPoolExecutor() as executor:
            reflector_futures = [executor.submit(decrypt, reflector, event) for reflector in reflectors]
            for reflector_future in as_completed(reflector_futures):
                if reflector_future.result():
                    break

    end = time.time()
    print(f"Code 3 parallel took:  {end - start}s")
