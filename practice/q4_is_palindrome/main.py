def is_palindrome(a:str) -> bool:
    if list(a) == list(reversed(a)):
        return True
    return False