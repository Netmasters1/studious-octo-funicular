"""
for value in range(3,30,3):
    print(value)

cube = []
for value in range(1,10):
    cube.append(value**3)
print(cube)

"""

cube = [value**3 for value in range(1,11)]
print(cube)