# Anagram Checker (freeCodeCamp)
#
# Given two strings, determine if they are anagrams of each other
# (contain the same characters in any order).
#
# Ignore casing and white space.
#
# Example:
# str1 = "Listen", str2 = "Silent"       -> True
# str1 = "The eyes", str2 = "They see"   -> True
# str1 = "hello", str2 = "world"         -> False


def is_anagram(str1: str, str2: str) -> bool:
    new_dictonary = {}
    new_dictonary2 = {}
    for x in str2:
        if x == " ":
            pass
        else:
            if x.lower() in new_dictonary:
                new_dictonary[x.lower()] += 1
            else:
                new_dictonary[x.lower()] = 1

    for x in str1:
        if x == " ":
            pass
        else:
            if x.lower() in new_dictonary2:
                new_dictonary2[x.lower()] += 1
            else:
                new_dictonary2[x.lower()] = 1

    return new_dictonary2 == new_dictonary
    


# Test cases
print(is_anagram("Listen", "Silent"))       # True
print(is_anagram("The eyes", "They see"))   # True
print(is_anagram("hello", "world"))         # False
