# Golf Handicap Calculator (freeCodeCamp)
#
# Given an array of golf scores and a corresponding array of course par
# values, return the golfer's handicap index using the following method:
#
# Calculate the differential for each round by subtracting the par from
# the score, then return the average of all differentials rounded to one
# decimal place.
#
# Example:
# scores = [85, 90, 80]
# pars   = [72, 72, 72]
# differentials = [13, 18, 8]
# average = 39 / 3 = 13.0

from decimal import Decimal, ROUND_HALF_UP
def golf_handicap(scores: list[int], pars: list[int]) -> float:

    diff = [s-p for s,p in zip(scores,pars)]
    if not diff:
        raise ValueError("scores/pars must not be empty")
    k = sum(diff) / len(diff)
    result = float(
    Decimal(str(k)).quantize(
            Decimal("0.1"),
            rounding=ROUND_HALF_UP
        )
    )

    return result

# Test cases
print(golf_handicap([42, 45, 46, 44], [36, 36, 36, 36]))
# Expected: 8.3

print(golf_handicap([95, 100, 89, 92], [70, 71, 69, 72]))
# Expected: 23.5

print(golf_handicap([72, 72, 72], [72, 72, 72]))
# # Expected: 0.0