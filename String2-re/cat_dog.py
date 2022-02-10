# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    if len(str) < 3:
        return True

    count1 = 0
    count2 = 0
    for i in range(len(str)-2):
      if str[i] + str[i+1] + str[i+2] == "cat":
          count1 = count1 + 1
      elif str[i] + str[i+1] + str[i+2] == "dog":
          count2 += 1
    return count1 == count2


print(cat_dog('catdog')) # True
print(cat_dog('catcat')) # False
print(cat_dog('1cat1cadodog'))# True