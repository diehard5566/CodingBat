# Given a string, return the count of the number of times that a substring length 2 appears in the string
# and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    count = 0
    last = str[-2:] #str[len(str)-2:]
    
    for i in range(0, len(str)-2, 1):
      if str[i:i+2] == last:
        count +=1
        
    return (count)
    
    

#
last2('xxxx') # 2

# last 2 char =str[:len(str)-2]