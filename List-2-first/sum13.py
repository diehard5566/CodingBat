
# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6
def sum13(nums):
    sum = 0
    for i in range(len(nums)-1):
        if nums[i] == 13:
            nums - nums[i] - nums[(i+1)]
            return sum(nums)
        elif nums[i] != 13 :
            return sum(nums)
        elif nums == []:
            return 0

def sum13(nums):

    if len(nums) == 0:
        return 0

    for i in range(0, len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i+1 < len(nums): 
                nums[i+1] = 0
    return sum(nums)
     

      
    
