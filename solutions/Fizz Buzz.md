# 412. Fizz Buzz

**Difficulty:** Easy
**Tags:** `Simulation`
**File:** `fizzbuzz/main.py`

---

## Problem

Given an integer `n`, return a string array where:
- `"FizzBuzz"` for multiples of both 3 and 5
- `"Fizz"` for multiples of 3
- `"Buzz"` for multiples of 5
- The number itself (as a string) otherwise

---

## Approach — Iteration with Conditionals

Check divisibility conditions in priority order (both → five → three → neither) and append the appropriate string.

```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        my_list = []
        for x in range(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                my_list.append("FizzBuzz")
            elif x % 5 == 0:
                my_list.append("Buzz")
            elif x % 3 == 0:
                my_list.append("Fizz")
            else:
                my_list.append(str(x))
        return my_list
```

**Time:** O(n)
**Space:** O(n)

---

[[Index]]
