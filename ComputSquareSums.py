## Problem: For the integer value provided in A, return the length of the
## smallest possible combination of squares that add up to that value.
## Example: 118 can be formed by adding 100, 9, and 9, so the answer is 3.
## Copyright 2015 Melodie Hardwick
import math

def answer(n):
    combo = []
    count = 1
    while len(combo) == 0:
        combo = []
        combo = getCombo(n, getCosts(n), count, [])
        count += 1

    return len(combo)

def getCombo(coins, costs, maxlength, stub = []):
    if (costs.count(coins) == 1):
        return [coins]

    for price in costs:
        if price > coins:
            continue
        if maxlength <= 1:
            return []

        newstub = getCombo((coins-price), costs, maxlength - 1, list(stub))
        if len(newstub) > 0:
            stub += [price] + newstub
            return stub
        
    return []

def getListSum(items):
    total = 0
    for item in items:
        total += item
    return total
        
def getSmallestComboSize():
    smallestcombo = 0

    for combo in combos:
        if smallestcombo == 0:
            smallestcombo = len(combo)
        elif smallestcombo > len(combo):
            smallestcombo = len(combo)
    return smallestcombo

def getCosts(max):
    costs = []

    size = 1
    while size <= math.sqrt(max):
        costs.insert(0, size*size)
        size += 1

    return costs

print answer(118)
