# using sets we can determine how many unique sides there are

def equilateral(sides):
    # Checking if all numbers are integers
    for i in sides:
        if float(i) != i:
            raise Exception("Inputs are not numbers")
    tri_set = set()
    for i, num in enumerate(sides):
        if sides[int(i)] > 0:
            tri_set.add(num)
    if len(tri_set) == 1:
        return True
    return False

def isosceles(sides):
    # Checking for if all numbers are integers
    for i in sides:
        if float(i) != i:
            raise Exception("Inputs are not numbers")
    tri_set = set()
    sides = sorted(sides)
    if sides[0] + sides[1] < sides[2]:
        return False
    for i in sides:
        tri_set.add(i)
    if len(tri_set) <= 2:
        return True
    return False

def scalene(sides):
    # Checking for if all numbers are integers
    for i in sides:
        if float(i) != i:
            raise Exception("Inputs are not numbers")
    tri_set = set()
    sides = sorted(sides)
    if sides[0] + sides[1] < sides[2]:
        return False
    for i in sides:
        tri_set.add(i)
    if len(tri_set) == 3:
        return True
    return False
