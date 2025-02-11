from enigma.decryption.code1 import decrypt
from enigma.enigma import Enigma
from enigma.plugboard import PlugBoard

if __name__ == '__main__':
    plug_board = PlugBoard()
    plug_board.add("WP")
    plug_board.add("RJ")
    plug_board.add("VF")
    plug_board.add("HN")
    plug_board.add("CG")
    plug_board.add("BS")

    rotors = [
        {"name": "V", "position": "M", "ring": 14},
        {"name": "Gamma", "position": "J", "ring": 2},
        {"name": "Beta", "position": "M", "ring": 4}]

    encrypted_msg = Enigma(plug_board, rotors, "A").encrypt("CAKESANDCO")
    print(encrypted_msg)

    # The below uses the same crib as above - bet you couldn't tell from the message alone. That's the power of Enigma
    # Can you guess?
    # other_encrypted_msg = "XLRNEIRVBVLOBKDYNVNXJHXI"
    # print(other_encrypted_msg)

    # Demonstrates use of a crib to compensate for missing configuration knowledge
    # decrypted_msg = decrypt(plug_board, rotors, "OPTO", encrypted_msg)
    # print(decrypted_msg)

    # decrypted_msg_v2 = decrypt(plug_board, rotors, "OPTO", other_encrypted_msg)
    # print(decrypted_msg_v2)
