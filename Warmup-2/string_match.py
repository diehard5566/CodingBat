# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    #判斷誰是比較長的str
    la = a #assume a is larger string
    sb = b #assume b is shorted string

    if len(a) < len(b):
        la = b
        sb = a

    count = 0
    for i in range(len(la)-1):#下面i+2所以這裡要-1
        #判斷長度為2的字串
        c = la[i:i+2]
        d = sb[i:i+2]
        if c == d:
            count += 1
    print(count)


string_match('xxcaazz', 'xxbaaz') # 3
string_match('abc', 'abc') # 2
string_match('abc', 'axc') # 0