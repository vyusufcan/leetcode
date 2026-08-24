# Message Decoder (freeCodeCamp)
#
# Given a secret message string, and an integer representing the number
# of letters that were used to shift the message to encode it, return
# the decoded string.
#
# A positive number means the message was shifted forward in the
# alphabet.
# A negative number means the message was shifted backward in the
# alphabet.
# Case matters, decoded characters should retain the case of their
# encoded counterparts.
# Non-alphabetical characters should not get decoded.
#
# Example:
# message = "ymj"   shift = 5    -> "the"   ('y' shifted back 5 -> 't', etc.)
# message = "Nla!"  shift = 7    -> "Get!"  ('!' stays as is)


def decode_message(message: str, shift: int) -> str:
    new_list = []
    for x in message:
        if x.isalpha():
            if x.isupper():
                location = ord(x) - ord("A")
                new_location = (location - shift) % 26
                new_char = chr(new_location + ord("A"))
                new_list.append(new_char)
            else:
                location = ord(x) - ord("a")
                new_location = (location - shift) % 26
                new_char = chr(new_location + ord("a"))
                new_list.append(new_char)
        else:
            new_list.append(x)

    return "".join(new_list)


# Test cases
print(decode_message("ymj", 5))     # the
print(decode_message("Nla!", 7))    # Get!
print(decode_message("khoor, zruog!", 3))  # hello, world!
