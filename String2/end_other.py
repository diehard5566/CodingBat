# Given two strings, return True if either of the strings appears at the very end of the other string, 
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
#  Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    lstr = a #assume a is larger string
    sstr = b #assume b is shorted string

    if len(b) > len(a):
        lstr = b
        sstr = a
    #         01234                     012345
    # lstr = "Hiabc"            lstr = "abXabc"
    #         012                       012
    # sstr = "abc"              sstr = "abc"
    #
    #lstr[5 -3 = 2 : 5]--->"abc"   lstr[6 - 3 = 3 :6]--->"abc"
    #General case - lstr[len(lstr) - len(sstr):len(lstr)]
    if sstr == lstr[len(lstr) - len(sstr): len(lstr)]:
        return True
    return False

    # if la[-1] == lb[-1]:
    #     return la[-1] == lb[-1] # lb[i:i+1] in la[:-1]
    #     or 

print(end_other('Hiabc', 'abc')) # True
print(end_other('AbC', 'HiaBc')) # True
print(end_other('abc', 'abXabc')) # True
print(end_other('Hiabcx', 'bc') )
print(end_other('Hiabc', 'abcd'))