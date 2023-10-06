import numpy

n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for x in range(n)])

arr_sum = numpy.sum(arr, axis=0)
result = numpy.prod(arr_sum, axis=0)
print(result)