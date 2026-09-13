# Array Diff (freeCodeCamp)
#
# Given two arrays with strings values, return a new array containing all
# the values that appear in only one of the arrays.
#
# - The returned array should be sorted in alphabetical order.
#
# Tests:
# 1. array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) should
#    return ["cherry"]
# 2. array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) should
#    return ["cherry"]
# 3. array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])
#    should return ["eight", "four", "six", "two"]
# 4. array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"])
#    should return ["five", "one", "seven", "three"]
# 5. array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) should
#    return ["freeCodeCamp", "rocks"]

def array_diff(arr1, arr2):

    k = list()
    for x in arr1:
        if x not in arr2:
            k.append(x)

    for x in arr2:
        if x not in arr1:
            k.append(x)


    return sorted(set(k))



print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))
print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
print(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]))
print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))
