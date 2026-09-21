# File Storage (freeCodeCamp)
#
# Given a file size, a unit for the file size, and hard drive capacity in
# gigabytes (GB), return the number of files the hard drive can store
# using the following constraints:
#
# - The unit for the file size can be bytes ("B"), kilobytes ("KB"), or
#   megabytes ("MB").
# - Return the number of whole files the drive can fit.
# - Use the following conversions.
#
# For example, given 500, "KB", and 1 as arguments, determine how many
# 500 KB files can fit on a 1 GB hard drive.



def number_of_files(file_size, unit, drive_capacity_gb):

    if unit == "KB":
        return int(drive_capacity_gb * 1000000 / file_size)
    elif unit == "MB":
        return int(drive_capacity_gb * 1000 / file_size)
    elif unit == "B":
        return int(drive_capacity_gb * 1000000000 / file_size)
    return None


print(number_of_files(500, "KB", 1))
print(number_of_files(2, "MB", 8))
print(number_of_files(50000, "B", 1))
print(number_of_files(4096, "B", 1.5))
