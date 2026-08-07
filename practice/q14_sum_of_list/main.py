def sum_list(lst: list) -> int:

    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1::])


# Test cases
print(sum_list([]))
# 0

print(sum_list([5]))
# 5

print(sum_list([1, 2, 3, 4]))
# 10
