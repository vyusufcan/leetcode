# 202. Happy Number

**Difficulty:** Easy
**Tags:** `Hash Map` `Math` `Two Pointers`
**File:** `happy_number/main.py`

---

## Problem

A **happy number** is defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat until the number equals 1 (happy), or it loops endlessly in a cycle (not happy).

**Examples:**
```
Input: n = 19  →  Output: true
  1² + 9² = 82
  8² + 2² = 68
  6² + 8² = 100
  1² + 0² + 0² = 1  ✓

Input: n = 2   →  Output: false  (enters a cycle)
```

---

## Approach — Seen Set (Cycle Detection)

Keep a list `c` of every number seen so far. On each iteration, compute the sum of squared digits. If it reaches `1`, return `True`. If the new number was already seen, a cycle exists — return `False`.

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        c = []
        while True:
            my_list = list(str(n))
            c.append(n)
            sum = 0
            for x in my_list:
                sum = sum + pow(int(x), 2)
            n = sum
            if n == 1:
                return True
            if n in c:
                return False
```

**Time:** O(log n) — the sequence shrinks quickly; membership check on a list is O(k)
**Space:** O(k) — stores all intermediate values until a cycle or 1 is found

---

## Better Approach — Floyd's Cycle Detection

Use a slow/fast pointer (tortoise and hare) on the sequence. No extra storage needed.

```python
def next_val(n):
    return sum(int(d) ** 2 for d in str(n))

slow, fast = n, next_val(n)
while fast != 1 and slow != fast:
    slow = next_val(slow)
    fast = next_val(next_val(fast))
return fast == 1
```

**Time:** O(log n)
**Space:** O(1)

---

[[Index]]
