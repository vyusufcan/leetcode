# 9. Palindrome Number

**Difficulty:** Easy
**Tags:** `Math`
**File:** `palindrome/main.py`

---

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

**Examples:**
```
Input: x = 121   →  Output: true   (reads same forwards and backwards)
Input: x = -121  →  Output: false  (negative numbers are never palindromes)
Input: x = 10    →  Output: false
```

---

## Approach — String Conversion

Convert the number to a list of characters, then compare it against its reverse.
Negative numbers short-circuit to `false` immediately.

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = list(str(x))
        reversed = k[::-1]
        if x < 0:
            return False
        if k == reversed:
            return True
        return False
```

**Time:** O(d) — where d is the number of digits
**Space:** O(d)

---

## Better Approach — No String Conversion

Reverse only the second half of the number mathematically and compare it to the first half.

**Time:** O(log n)
**Space:** O(1)

---

[[Index]]
