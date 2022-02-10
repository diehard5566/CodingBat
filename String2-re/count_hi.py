# Return the number of times that the string "hi" appears anywhere in the given string.

from itertools import count


def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i] == "h" and str[i+1] == "i":
            count = count + 1
    return count 

print(count_hi('abc hi ho')) # 1
print(count_hi('ABChi hi')) # 2
print(count_hi('hihi')) # 2

#return str.count("hi")