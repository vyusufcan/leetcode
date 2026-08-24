# Morse Code (freeCodeCamp)
#
# Given a Morse code string, return the decoded message using the
# following table:
#
# Code     Letter    Code     Letter
# .-       A         -.       N
# -...     B         ---      O
# -.-.     C         .--.     P
# -..      D         --.-     Q
# .        E         .-.      R
# ..-.     F         ...      S
# --.      G         -        T
# ....     H         ..-      U
# ..       I         ...-     V
# .---     J         .--      W
# -.-      K         -..-     X
# .-..     L         -.--     Y
# --       M         --..     Z
#
# Letters are separated by a single space.
# Words are separated by three spaces.
#
# Example:
# code = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
# ->    "HELLO WORLD"


MORSE_TO_LETTER = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
}


def decode_morse(code: str) -> str:
    my_list = list()
    for x in code.split("  "):
        for k in x.split(" "):
            if k not in MORSE_TO_LETTER:
                my_list.append(' ')
            else:
                my_list.append(MORSE_TO_LETTER[k])



    return ''.join(my_list) 

   

# Test cases
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))  # HELLO WORLD
print(decode_morse(("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.")))
print(decode_morse("... --- ..."))                                  # SOS
print(decode_morse("-.-. --- -.. ."))                                # CODE
