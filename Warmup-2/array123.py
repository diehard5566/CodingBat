# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  if len(nums) <= 2:
    return False

  for i in range(len(nums)+3):
      if nums[i:i+3] == [1, 2, 3]:
        return True
  return False

array123([1, 1, 2, 3, 1])
print(array123([1, 1, 2, 3, 1])) # True
print(array123([1, 1, 2, 4, 1])) # False
print(array123([1, 1, 2, 1, 2, 3])) # True