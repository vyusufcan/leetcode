# Thermostat Adjuster (freeCodeCamp)
#
# Given the current temperature of a room and a target temperature, return
# a string indicating how to adjust the room temperature based on these
# constraints:
#
# - Return "heat" if the current temperature is below the target.
# - Return "cool" if the current temperature is above the target.
# - Return "hold" if the current temperature is equal to the target.

def adjust_thermostat(current_temp, target_temp):
    if current_temp < target_temp:
        return "heat"
    elif current_temp > target_temp:
        return "cool"
    elif current_temp == target_temp:
        return "hold"
    else:
        return None
    


print(adjust_thermostat(65, 70))
print(adjust_thermostat(75, 70))
print(adjust_thermostat(70, 70))
print(adjust_thermostat(-20.5, -10.1))
print(adjust_thermostat(100, 99.9))
print(adjust_thermostat(0.0, 0.0))
