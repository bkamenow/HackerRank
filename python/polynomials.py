import numpy

P = list(map(float, input().split()))
x = int(input())

result = numpy.polyval(P, x)

print(result)
