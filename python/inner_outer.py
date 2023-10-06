import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr_inner = numpy.inner(A, B)
arr_outer = numpy.outer(A, B)

print(arr_inner)
print(arr_outer)
