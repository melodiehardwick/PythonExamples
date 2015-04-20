## Problem: given a list of names, compute and sort by their numerical value.
## Numerical value is calculated by adding up the letters (A=1, B=2, etc.)
## If two names have equal value, the name with the highest values in the first letters go first.
## Copyright 2015 Melodie Hardwick

def answer(names):
    calculatednames = []
    for name in names:
        namevalue = calcValue(name)
        calculatednames.append((namevalue, name))

    sortednames = sortnames(calculatednames)
    strippednames = []
    for sortedname in sortednames:
        strippednames.append(sortedname[1])
    return strippednames

def sortnames(calculatednames):
    sortednames = []

    count = 0
    while count < len(calculatednames):
        calculatedname = calculatednames[count]
        if len(sortednames) == 0:
            sortednames.append(calculatedname)
        else:
            sortcount = 0
            index = -1
            while sortcount < len(sortednames):
                name = sortednames[sortcount]
                if calculatedname[0] < name[0]:
                    sortcount += 1
                    continue
                if calculatednames[count][0] == name[0]:
                    if calculatedname[1] > name[1]:
                        index = sortcount
                        break
                    else:
                        sortcount += 1
                        continue
                if calculatedname[0] > name[0]:
                    index = sortcount
                    break
                    
                sortcount += 1

            if index >= 0:
                sortednames.insert(index, calculatedname)
            else:
                sortednames.append(calculatedname)

        count += 1
    
    return sortednames

def calcValue(name):
    total = 0
    for letter in name:
        total += ord(letter) - 96
    return total


names = ["bonnie", "qickld", "annie", "pickle"]
print answer(names)

names = ["abcdefg", "vi"]
print answer(names)

names = ["annie", "bonnie", "liz"]
print answer(names)

