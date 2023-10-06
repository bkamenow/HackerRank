import numpy

n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for x in range(n)])

arr_min = numpy.min(arr, axis=1)
arr_max = numpy.max(arr_min, axis=0)

print(arr_max)