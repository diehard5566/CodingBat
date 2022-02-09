# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.).
#  So "xxyz" counts but "x.xyz" does not.
#      0123456789 
#str = abc.xyzxyz
#      xixx


def xyz_there(str):
    if len(str) >= 3 and str[0:3] == "xyz":
        return True

    for i in range(1, len(str)-2):
        if str[i-1] !=  "." and str[i:i+3] == "xyz":
            return True

    return False

print(xyz_there('abcxyz')) # True
print(xyz_there('abc.xyz')) # False
print(xyz_there('xyz.abc')) # True
print(xyz_there('abc.xyzxyz')) # True
print(xyz_there('abc.xxyz')) # True
print(xyz_there('12xyz')) # True

#return str.count("xyz") - str.count(".xyz") > 0