# RGB to Hex (freeCodeCamp)
#
# Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.
#
# Examples:
# rgb_to_hex("rgb(255, 255, 255)") -> "#ffffff"
# rgb_to_hex("rgb(1, 2, 3)") -> "#010203"
#
# - Make any letters lowercase.
# - Return a # followed by six characters. Don't use any shorthand values.
#
# Tests:
# 1. rgb_to_hex("rgb(255, 255, 255)") should return "#ffffff"
# 2. rgb_to_hex("rgb(1, 11, 111)") should return "#010b6f"
# 3. rgb_to_hex("rgb(173, 216, 230)") should return "#add8e6"
# 4. rgb_to_hex("rgb(79, 123, 201)") should return "#4f7bc9"

def rgb_to_hex(rgb_string):

    x= rgb_string.replace("rgb", "").replace("(","").replace(")","").replace(" ","")
    k = []
    for x in x.split(","):
        hex_value = hex(int(x)).replace("0x","")
        if len(hex_value) == 1:
            s = "0" + hex_value
            k.append(s)
        else:
            k.append(hex_value)
    return "#"+"".join(k)
            
            


print(rgb_to_hex("rgb(255, 255, 255)"))
print(rgb_to_hex("rgb(1, 11, 111)"))
print(rgb_to_hex("rgb(173, 216, 230)"))
print(rgb_to_hex("rgb(79, 123, 201)"))
