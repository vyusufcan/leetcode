# 13. Roman to Integer

**Difficulty:** Easy
**Tags:** `Hash Map` `String`
**File:** `romanian/main.py`

---

## Problem

Given a roman numeral string `s`, convert it to an integer.

| Symbol | Value |
|--------|-------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

**Subtraction rule:** when a smaller symbol appears before a larger one (e.g. `IV = 4`, `IX = 9`), subtract the smaller value.

---

## Approach — Left-to-Right Scan

Iterate through all characters except the last. If the current symbol's value is less than the next one, subtract it; otherwise add it. Always add the last symbol.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        x = list(s)
        sum = 0
        for k in range(len(x) - 1):
            if symbols[x[k]] < symbols[x[k+1]]:
                sum -= symbols[x[k]]
            else:
                sum += symbols[x[k]]
        sum += symbols[x[-1]]
        return sum
```

**Time:** O(n)
**Space:** O(1) — the symbol dict is fixed size

---

[[Index]]
