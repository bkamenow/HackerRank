import numpy


def arrays(arr):
    num_array = numpy.array(arr, dtype=float)
    reversed_array = numpy.flip(num_array)
    return reversed_array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
