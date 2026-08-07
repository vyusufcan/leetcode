# 69. Sqrt(x)

**Difficulty:** Easy
**Tags:** `Math` `Binary Search`
**File:** `sqrt/main.py`

---

## Problem

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or square root function.

**Examples:**
```
Input: x = 4  →  Output: 2
Input: x = 8  →  Output: 2  (√8 ≈ 2.828, floored to 2)
```

---

## Approach — Built-in Power Operator

Use Python's `**` operator with exponent `0.5` and cast to `int` to floor the result.

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** (1/2))
```

**Time:** O(1)
**Space:** O(1)

> Note: the problem statement says to avoid built-in sqrt/exponent functions. This solution uses `**` which technically bypasses that constraint.

---

## Better Approach — Binary Search

Search for the largest integer `mid` such that `mid * mid <= x`.

```python
left, right = 0, x
while left <= right:
    mid = (left + right) // 2
    if mid * mid == x:
        return mid
    elif mid * mid < x:
        left = mid + 1
    else:
        right = mid - 1
return right
```

**Time:** O(log n)
**Space:** O(1)

---

[[Index]]
