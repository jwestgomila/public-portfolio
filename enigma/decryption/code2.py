from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard

def get_rotors(positions):
    return [
        {"name": "III", "position": positions[0], "ring": 10},
        {"name": "I", "position": positions[1], "ring": 2},
        {"name": "Beta", "position": positions[2], "ring": 23}]

def decrypt(enigma_generator, crib, message):
    for i in range(25):
        for j in range(25):
            for k in range(25):
                positions = [chr(ord("A") + i), chr(ord("A") + j), chr(ord("A") + k)]
                rotors = get_rotors(positions)
                enigma = enigma_generator(rotors)
                result = enigma.encrypt(message)
                if result.find(crib) > -1:
                    print(f"Found result '{result}'")
                    print(f"Found position setting '{positions}'")
                    return positions

if __name__ == '__main__':
    plug_board = PlugBoard()
    plug_board.add("VH")
    plug_board.add("PT")
    plug_board.add("ZG")
    plug_board.add("BJ")
    plug_board.add("EY")
    plug_board.add("FS")

    enigma_generator = lambda x: Enigma(plug_board, x, "B")
    decrypt(enigma_generator, "UNIVERSITY", "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH")
