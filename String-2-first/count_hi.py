# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    count = str.count('hi')
    return count

print(count_hi('abc hi ho') == 1)
print(count_hi('hi hi hi') == 3)
print(count_hi('g b h') == 0)

#不用.count() function 的話要這樣
# def count_hi(str):
#     count = 0
#     for i in range(len(str)-1):#為了可以i+1所以這邊要先-1，不然i+1的時候會超過
#       if str[i] + str[(i + 1)] == 'hi':
#         count = count + 1
#     return count

