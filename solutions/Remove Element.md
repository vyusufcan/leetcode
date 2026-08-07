# 27. Remove Element

**Difficulty:** Easy
**Tags:** `Array` `Two Pointers`
**File:** `remove_element/main.py`

---

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. Return the number of elements remaining.

**Examples:**
```
Input: nums = [3,2,2,3], val = 3  →  Output: 2  (nums becomes [2,2,...])
Input: nums = [0,1,2,2,3,0,4,2], val = 2  →  Output: 5
```

---

## Approach — Repeated Removal

Iterate `len(nums)` times. On each pass, if `val` is still present in the list, call `list.remove()` which removes the first occurrence.

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for x in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)
```

**Time:** O(n²) — `in` and `remove` are each O(n), called up to n times
**Space:** O(1)

---

## Better Approach — Two Pointers

Use a write pointer `k` that only advances when the current element is not `val`.

```python
k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
return k
```

**Time:** O(n)
**Space:** O(1)

---

[[Index]]
