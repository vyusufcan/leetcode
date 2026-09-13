# camelCase (freeCodeCamp)
#
# Given a string, return its camel case version using the following rules:
#
# Words in the string argument are separated by one or more characters from
# the following set: space ( ), dash (-), or underscore (_). Treat any
# sequence of these as a word break.
# The first word should be all lowercase.
# Each subsequent word should start with an uppercase letter, with the rest
# of it lowercase.
# All spaces and separators should be removed.
#
# Example:
# "the-stealth-warrior"   -> "theStealthWarrior"
# "The_Stealth_Warrior"   -> "theStealthWarrior"
# "The Stealth-Warrior"   -> "theStealthWarrior"

import re
def to_camel_case(text: str) -> str:
    
    text = re.sub("[-_]", " ", text)
    k = text.lower().split(' ')
    unique = [x for x in k if x != '']
    res = unique[0] + ''.join(word.capitalize() for word in unique[1:])
    return res  
    


# Test cases
print(to_camel_case("-hello world"))
print(to_camel_case("__hello world"))
print(to_camel_case("_ hello world"))  
print(to_camel_case("hello world"))           
print(to_camel_case("HELLO WORLD"))   
print(to_camel_case("secret agent-X"))    
print(to_camel_case("FREE cODE cAMP"))    
print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))  
