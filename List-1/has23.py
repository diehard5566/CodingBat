
# Given an int array length 2, return True if it contains a 2 or a 3.

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False
def has23(nums):
    if nums[0] == 2 or nums[1] ==  3 or nums[1] == 2 or nums[0] ==  3:
        return True
    else:
        return False

print(has23([4, 3]) == True)
print(has23([5, 5]) == False)
print(has23([1, 1]) == False)
print(has23([2, 3]) == True)
print(has23([3, 2]) == True)