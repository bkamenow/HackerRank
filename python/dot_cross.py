import numpy

n = int(input())

A = numpy.array([list(map(int, input().split())) for x in range(n)])
B = numpy.array([list(map(int, input().split())) for i in range(n)])

result = numpy.dot(A, B)

print(result)
