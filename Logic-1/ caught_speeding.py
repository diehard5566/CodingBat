# You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
# encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, 
# your speed can be 5 higher in all cases.

# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
     if speed <= 65 :
        return 0
     elif speed >=66 and speed <=85:
        return 1
     elif speed >=86:
        return 2 
      
  if is_birthday == False:
    if speed <= 60 :
      return 0
    elif speed >=61 and speed <=80:
      return 1
    elif speed >=81:
      return 2
  
print(caught_speeding(60, False) == 0)
print(caught_speeding(85, False) == 2)
print(caught_speeding(85, True) == 1)
    
# def caught_speeding(speed, is_birthday):
#   speeding = speed - (65 if is_birthday else 60)
#   if speeding > 20:
#     return 2
#   elif speeding > 0:
#     return 1
#   else:
#     return 0
# 更簡潔的寫法