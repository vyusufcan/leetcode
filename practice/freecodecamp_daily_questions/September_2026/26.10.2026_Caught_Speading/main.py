# Caught Speeding
# Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

# If there were no vehicles speeding, return [0, 0].



def speeding(speeds, limit):

    caught = []
    tmp = []
    counter = 0

    for speed in speeds:
        if speed > limit:
            counter = counter +1
            tmp.append(speed-limit)

    if counter == 0:
        return [0,0]

    average = sum(tmp) / len(tmp)

    if average.is_integer():
        average = int(average)

    caught.append(counter)
    caught.append(average)
    return caught


print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([100, 105, 95, 102], 100))
print(speeding([40, 45, 44, 50, 112, 39], 55))
print(speeding([58, 50, 60, 55], 55)) # [2,4]
print(speeding([50, 60, 55], 60))