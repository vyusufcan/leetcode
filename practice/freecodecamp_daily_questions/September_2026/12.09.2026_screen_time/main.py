# Screen Time
# Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

# If any single day has 10 hours or more, it's too much.
# If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
# If the average of the seven days is greater than or equal to 6 hours, it's too much.

def too_much_screen_time(hours):

    if 10 in hours:
        return True

    for x in hours:
        if x > 10:
            return True

    if (sum(hours) / len(hours)) >= 6:
        return True
    

    for k in range(0,5):
        if (hours[k] + hours[k+1] + hours[k+2])/3 >= 8:
            return True

    return False

        


# 1 
# 2 3

# 2
# 3 10

# 3
# 10 2

# 10
# 2 1

# 2
# 1 0

print(too_much_screen_time([1, 2, 3, 4, 5, 6, 7])) #False
# print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0])) #True

# print(too_much_screen_time([1, 2, 3, 11, 1, 3, 4])) #True
# print(too_much_screen_time([3, 3, 5, 8, 8, 9, 4])) #True

# print(too_much_screen_time([3, 9, 4, 8, 5, 7, 6])) #True