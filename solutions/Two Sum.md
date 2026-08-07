# 1. Two Sum

**Difficulty:** Easy
**Tags:** `Array` `Hash Map`
**File:** `two_sums/main.py`

---

## Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`. Each input has exactly one solution and you may not use the same element twice.

**Examples:**
```
Input:  nums = [2,7,11,15], target = 9  →  Output: [0,1]
Input:  nums = [3,2,4],     target = 6  →  Output: [1,2]
Input:  nums = [3,3],       target = 6  →  Output: [0,1]
```

---

## Approach — Brute Force

Check every pair `(i, j)` where `j > i`. If `nums[i] + nums[j] == target`, return both indices.

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**Time:** O(n²) — nested loops over all pairs
**Space:** O(1)

---

## Better Approach — Hash Map

Store each number's index in a dict. For each element, check if its complement (`target - num`) is already in the dict.

**Time:** O(n)
**Space:** O(n)

---

[[Index]]
