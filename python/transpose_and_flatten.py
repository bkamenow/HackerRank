import numpy

n, m = map(int, input().split())

arr = numpy.array([input().split() for _ in range(n)], dtype=int)

transposed_arr = numpy.transpose(arr)

flattened_arr = arr.flatten()

print(transposed_arr, flattened_arr, sep='\n')
