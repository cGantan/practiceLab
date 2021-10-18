'''
You have two version strings composed of several non-negative decimal fields that are separated by periods ("."). Both strings contain an equal number of numeric fields. Return 1 if the first version is higher than the second version, -1 if it is smaller, and 0 if the two versions are the same.
'''
def higherVersion2(ver1, ver2):
    period = "."
    while period in ver1:
        one = int(ver1[:ver1.index(period)])
        two = int(ver2[:ver2.index(period)])
        if (one > two):
            return 1
        elif (one < two):
            return -1
        ver1 = ver1[ver1.index(period)+1 :]
        ver2 = ver2[ver2.index(period)+1 :]
    if int(ver1) == int(ver2):
        return 0
    elif int(ver1) > int(ver2):
        return 1
    return -1
