import numpy

n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for x in range(n)])

arr_mean = numpy.mean(arr, axis=1)
arr_var = numpy.var(arr, axis=0)
arr_std = numpy.std(arr, axis=None)

rounded_arr_std = numpy.round(arr_std, decimals=11)

print(arr_mean)
print(arr_var)
print(rounded_arr_std)