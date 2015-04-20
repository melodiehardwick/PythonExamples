## Problem: given three integer values, write a function called "answer"
## that returns the date, if the three values can be used to form one date.
## Return "Ambiguous" if more than one can be formed.
## Copyright 2015 Melodie Hardwick

def answer(x, y, z):
    dates = []
    if canBeMonth(x):
        if canBeDay(y, x, z):
            if canBeYear(z):
                date = "%02d/%02d/%02d" % (x, y, z)
                if dates.count(date) == 0:
                    dates.append(date)
        if canBeDay(z, x, y):
            if canBeYear(y):
                date = "%02d/%02d/%02d" % (x, z, y)
                if dates.count(date) == 0:
                    dates.append(date)
    if canBeMonth(y):
        if canBeDay(x, y, z):
            if canBeYear(z):
                date = "%02d/%02d/%02d" % (y, x, z)
                if dates.count(date) == 0:
                    dates.append(date)
        if canBeDay(z, y, x):
            if canBeYear(x):
                date = "%02d/%02d/%02d" % (y, z, x)
                if dates.count(date) == 0:
                    dates.append(date)
    if canBeMonth(z):
        if canBeDay(x, z, y):
            if canBeYear(y):
                date = "%02d/%02d/%02d" % (z, x, y)
                if dates.count(date) == 0:
                    dates.append(date)
        if canBeDay(y, z, x):
            if canBeYear(x):
                date = "%02d/%02d/%02d" % (z, y, x)
                if dates.count(date) == 0:
                    dates.append(date)
                    
    if len(dates) != 1:
        return "Ambiguous"
    return dates[0]

def canBeMonth(x):
    if (x > 0) & (x < 13):
        return True
    return False

def canBeYear(x):
    if (x > 0) & (x < 100):
        return True
    return False

def canBeDay(x, month, year):
    if (x <= 0) & (x > 31):
        return False
    if (month == 9) | (month == 4) | (month == 6) | (month == 11):
        if (x <= 30):
            return True
    elif (month == 2):
        if (x <= 28):
            return True
        elif x == 29:
            if (year % 4) > 0:
                return False
            elif (year % 400) == 0:
                return True
            elif (year % 100) == 0:
                return False
            else:
                return True
    else:
        return True
    return False
