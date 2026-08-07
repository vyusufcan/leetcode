def count_vowels(a:str) -> int:
    
    vowels = ["a", "e", "i", "o", "u"]
    sum = 0
    for x in a:
        for k in vowels:
            if x.lower() == k:
                sum = sum + 1
    return sum


# def count_vowels(a: str) -> int:
#       vowels = "aeiou"
#       count = 0
#       for x in a:
#           if x.lower() in vowels:
#               count += 1
#       return count

# def count_vowels(a: str) -> int:
#       return sum(1 for x in a if x.lower() in "aeiou")