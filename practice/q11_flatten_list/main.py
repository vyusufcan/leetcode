def flatten(lst: list) -> list:

    new_list =[]
    for x in lst:
        if isinstance(x ,list):
            new_list.extend(flatten(x))
        else:
            new_list.append(x)

    return new_list
            




# Test cases
print(flatten([1, [2, 3], [4, [5, 6]], 7]))
# [1, 2, 3, 4, 5, 6, 7]

print(flatten([[1, 2], [3, [4, [5]]]]))
# # [1, 2, 3, 4, 5]

print(flatten([1, 2, 3]))
# # [1, 2, 3]
