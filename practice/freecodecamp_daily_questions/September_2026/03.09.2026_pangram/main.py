# Pangram (freeCodeCamp)
#
# Given a word or sentence and a string of lowercase letters, determine if
# the word or sentence uses all the letters from the given set at least once
# and no other letters.
#
# - Ignore non-alphabetical characters in the word or sentence.
# - Ignore letter casing in the word or sentence.
#
# Examples:
# is_pangram("hello", "helo") -> True
# is_pangram("hello", "hel") -> False
# is_pangram("hello", "helow") -> False
# is_pangram("hello world", "helowrd") -> True
# is_pangram("Hello World!", "helowrd") -> True
# is_pangram("Hello World!", "heliowrd") -> False
# is_pangram("freeCodeCamp", "frcdmp") -> False
# is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") -> True

def is_pangram(text, letters):

    x = {c.lower() for c in letters if c.isalpha()}
    y = {c.lower() for c in text if c.isalpha()}
    if x == y:
        return True
    return False
           


print(is_pangram("hello", "helo")) #True
print(is_pangram("hello", "hel")) #False
print(is_pangram("hello", "helow")) #False
print(is_pangram("hello world", "helowrd")) #True
print(is_pangram("Hello World!", "helowrd")) #True
print(is_pangram("Hello World!", "heliowrd"))
print(is_pangram("freeCodeCamp", "frcdmp"))
print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))
