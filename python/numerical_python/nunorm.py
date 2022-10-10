import numpy as np

def norm():

    sequence = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001]
    v = 1.2
    sum = 0
    i = 0

    while i < len(sequence):
        sum += sequence[i]*np.power(v, i)
        i += 1
        print(sum)


norm()