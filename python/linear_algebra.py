import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
determinant = numpy.linalg.det(a)

print(round(determinant, 2))