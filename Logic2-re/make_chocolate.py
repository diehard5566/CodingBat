# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
    if goal > (big * 5)+small:
        return -1
    elif goal % 5 > small:
        return -1
    elif big * 5 > goal:
      return goal % 5 
    return goal - big * 5

make_chocolate(4, 1, 9) # 4
make_chocolate(4, 1, 10) # -1
make_chocolate(4, 1, 7) # 2
