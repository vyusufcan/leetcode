# Army Battle (freeCodeCamp)
#
# Given two strings representing your army and an opposing army, each
# character from your army battles the character at the same position
# from the opposing army using the following rules:
#
# Characters a-z have a strength of 1-26, respectively.
# Characters A-Z have a strength of 27-52, respectively.
# Digits 0-9 have a strength of their face value.
# All other characters have a value of zero.
# Each character can only fight one battle.
# For each battle, the stronger character wins. The army with more
# victories, wins the war. Return the following values:
#
# "Opponent retreated" if your army has more characters than the opposing
# army.
# "We retreated" if the opposing army has more characters than yours.
# "We won" if your army won more battles.
# "We lost" if the opposing army won more battles.
# "It was a tie" if both armies won the same number of battles.
#
# Example:
# army_battle("abc", "ABC") -> "We lost" (a<A, b<B, c<C, opponent wins all 3)
# army_battle("aaa", "bb")  -> "Opponent retreated" (your army is longer)

import string
def army_battle(your_army: str, their_army: str) -> str:

    if len(your_army) > len(their_army):
        return "Opponent retreated"
    elif len(their_army) > len(your_army):
       return "We retreated"
    else:
        lowercase_alphabet = string.ascii_lowercase
        uppercase_alphabet = string.ascii_uppercase

        lowerscase_score = {}
        lowercase_counter = 0

        uppercase_score = {}
        uppercase_counter = 26

        for x in lowercase_alphabet:
            lowercase_counter = lowercase_counter + 1
            lowerscase_score[x] = lowercase_counter

        for x in uppercase_alphabet:
                uppercase_counter = uppercase_counter + 1
                uppercase_score[x] = uppercase_counter

        team = list(zip(your_army,their_army))

        general_your_army_score = 0
        general_their_army_score = 0
        
        for x in team:
            your_army_score = 0
            their_army_score = 0

            if x[0] in lowerscase_score:
                your_army_score = lowerscase_score[x[0]] + your_army_score
            if x[0] in uppercase_score:
                your_army_score = uppercase_score[x[0]] + your_army_score
            if x[0].isdigit():
                your_army_score = int(x[0]) + your_army_score
                

            if x[1] in lowerscase_score:
                their_army_score = lowerscase_score[x[1]] + their_army_score
            if x[1] in uppercase_score:
                their_army_score = uppercase_score[x[1]] + their_army_score
            if x[1].isdigit():
                their_army_score = int(x[1]) + their_army_score

            if your_army_score > their_army_score:
                general_your_army_score = general_your_army_score + 1
            elif your_army_score < their_army_score:
                general_their_army_score = general_their_army_score + 1
            else:
                 general_their_army_score = general_their_army_score + 0
                 general_your_army_score = general_your_army_score + 0

        if general_your_army_score > general_their_army_score:
            return "We won"
        elif general_your_army_score < general_their_army_score:
            return "We lost"
        else:
            return "It was a tie"

# Test cases
print(army_battle("kn!ght", "orc"))
# print(army_battle("PC", "Mac"))
# print(army_battle("pizza", "salad"))
# print(army_battle("Hello", "World"))
# print(army_battle("Wizards", "Dragons"))
# print(army_battle("aaa", "bb"))
# print(army_battle("9a", "1b"))  # expected: It was a tie ('9'=9 > '1'=1, but 'a'=1 < 'b'=2)
