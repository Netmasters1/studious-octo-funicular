"""
cubes = []
for value in range(1,12):
    cubes.append(value**3)
print(cubes)

"""
digits = list(range(1,1000001,+1))
assert min(digits) == 1
assert max(digits) == 1000000

total = sum(digits)
print(total)