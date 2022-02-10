# Return the "centered" average of an array of ints, 
# which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
#  Use int division to produce the final average. You may assume that the array is length 3 or more.

# Find the sum of the list and take off the largest and smallest values 
# then divide by length of the list minus 2(cuz need take off largest and smallest value)

def centered_average(nums):
    max1 = nums[0]
    min1 = nums[0]
    
    sum = 0
    for i in range(0, len(nums)):
        sum = sum + nums[i]
        if nums[i] > max1:
            max1 = nums[i]
        if nums[i] < min1:
            min1 = nums[i]
            # can sort like
        # max1 = max(max1,nums[i])
        # min1 = min(min1,nums[i])
        
    return (sum - max1 - min1) / (len(nums)-2)

print(centered_average([1, 2, 3, 4, 100])) # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7])) # 5
print(centered_average([-10, -4, -2, -4, -2, 0])) # -3

# return (sum(nums) - max(nums) - min(nums)) / (len(nums)-2)  <-cleanest