## Problem: contagion calculation in grids. Given a population grid filled
## with resistance values, a starting point of X, Y, and a virust strength values,
## return a grid filled with -1 for each member of the population who could
## obtain the virus from an infected neighbor and did not have resistance
## greater than the virus strength.real
## Copyright 2015 Melodie Hardwick
def answer(population, x, y, strengh):
    height = len(population)
    if (height == 0) | (y >=  height) | (y < 0):
        return population
    width = len(population[0])
    if (width == 0) | (x >= width) | (x < 0):
        return population
    
    if population[y][x] == -1:
        return population

    if population[y][x] <= strength:
        population[y][x] = -1
    else:
        return population
    
    coordinates = getAdjacentCoordinates(x, y, width, height)

    for coordinate in coordinates:
        population = answer(population, coordinate[0], coordinate[1], strength)

    return population

def getAdjacentCoordinates(x, y, gridwidth, gridheight):
    coordinates = []
    if (x >= gridwidth) | (y >= gridheight):
        return coordinates
    if (x > 0):
        coordinates.append((x-1, y))
    if (y > 0):
        coordinates.append((x, y-1))
    if (y < gridheight-1):
        coordinates.append((x+1, y))
    if (x < gridwidth-1):
        coordinates.append((x, y+1))

    return coordinates

population = [[6,7,2,7,6], [6,3,1,4,7], [0,2,4,1,10], [8,1,1,4,9]]
x = 4
y = 3
strength = 15

print answer(population, x, y, strength)
