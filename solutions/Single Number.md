# 136. Single Number

**Difficulty:** Easy
**Tags:** `Hash Map` `Bit Manipulation`
**File:** `single_number/main.py`

---

## Problem

Given a non-empty array `nums` where every element appears twice except for one, return the element that appears only once.

**Examples:**
```
Input: nums = [2,2,1]       →  Output: 1
Input: nums = [4,1,2,1,2]   →  Output: 4
Input: nums = [1]           →  Output: 1
```

---

## Approach — Frequency Map

Count occurrences of each number in a dict, then return the key whose value is `1`.

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        my = {}
        for x in nums:
            sum = 1
            if my.get(x):
                sum += sum
                my[x] = sum
            else:
                my[x] = sum

        for key, val in my.items():
            if val == 1:
                return key
```

**Time:** O(n)
**Space:** O(n)

---

## Better Approach — XOR

XOR every element together. Since `a ^ a = 0` and `a ^ 0 = a`, all duplicate pairs cancel out, leaving only the unique element.

```python
from functools import reduce
return reduce(lambda a, b: a ^ b, nums)
```

**Time:** O(n)
**Space:** O(1)

---

[[Index]]
