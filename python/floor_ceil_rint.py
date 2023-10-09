import numpy
numpy.set_printoptions(legacy='1.13')

arr = numpy.array(input().split(), float)

result = [numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr)]

for i in result:
    print(i)
