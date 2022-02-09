# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) < 2:
        return str   

    for i in range(len(str)):
        new = str[-1] + str[1:-1] + str[0]
    return new


print(front_back('code')) # 'eodc'
print(front_back('a')) # 'a'
print(front_back('ab')) # 'ba'

print(front_back('hello'))
print(front_back('Chocolate'))