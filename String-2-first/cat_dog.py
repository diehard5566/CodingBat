# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  count1 = 0
  count2 = 0
  for i in range(len(str)-2):
    if str[i] + str[i+1] + str[i+2] == 'cat':
      count1 += 1
    elif str[i] + str[i+1] + str[i+2] == 'dog':
      count2 += 1
  return count1 == count2

