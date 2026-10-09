# Longest Word
# Given a sentence, return the longest word in the sentence.

# Ignore periods (.) when determining word length.
# If multiple words are ties for the longest, return the first one that occurs.




def get_longest_word(sentence):

    k = {}
    for x in sentence.split(" "):
        c = x.replace(".","")
        k[c] = len(c)
    return max(k, key=k.get)
     



print(get_longest_word("coding is fun")) #"coding"
print(get_longest_word("Coding challenges are fun and educational."))