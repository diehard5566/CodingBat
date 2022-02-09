# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
    sum = 0
    if len(nums) > 0 and nums[0] != 13:
        sum = nums[0] 

    for i in range(1, len(nums)):
      if nums[i] != 13 and nums[i-1] != 13:
          sum = sum + nums[i]


    return sum


print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6