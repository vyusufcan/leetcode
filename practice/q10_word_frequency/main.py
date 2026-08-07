def word_frequency(s: str) -> dict:
    word_count = {}
    for x in s.split():
        if x.lower() in word_count:
            word_count[x.lower()] += 1
        else:
            word_count[x.lower()] = 1
    return word_count


# # Test cases
print(word_frequency("the cat sat on the mat the cat ran"))
# {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1, "ran": 1}

print(word_frequency("Hello hello world"))
# {"hello": 2, "world": 1}

print(word_frequency("hello world hello"))
# {"hello": 2, "world": 1}
