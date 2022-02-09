# Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
# Return 0 for no numbers.


def sum67(nums):
    flags = True
    sum = 0
    for i in range(0, len(nums), 1):
        if nums[i] == 6:
            flags = False
        elif flags == False and nums[i] == 7 :
            flags = True
        elif flags == True:
         sum = sum + nums[i]    
    return sum
      
sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) # 2
print(sum67([1, 2, 2])) # 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 1, 6, 7, 2])) # 4

#nums[i:(nums[i]+1)]  6-7

#nums[nums[i]:(nums[i]-1)]