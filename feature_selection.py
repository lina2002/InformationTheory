import itertools
import math


def mutual_information(x, y):
    xy = list(zip(x, y))
    l = len(x)
    mi = 0
    binary_sequences = list(itertools.product([0, 1], repeat=2))
    for (i, j) in binary_sequences:
        if xy.count((i, j)):
            mi += (xy.count((i, j)) / l) * math.log2((xy.count((i, j)) * l) / (x.count(i) * y.count(j)))
    return mi

def mutual_information_3(x, y, z):
    xy = list(zip(x, y))
    xyz = list(zip(x, y, z))
    l = len(x)
    mi = 0
    binary_sequences = list(itertools.product([0, 1], repeat=3))
    for (i, j, k) in binary_sequences:
        if xyz.count((i, j, k)):
            mi += (xyz.count((i, j, k)) / l) * math.log2((xyz.count((i, j, k)) * l) / (xy.count((i, j)) * y.count(k)))
    return mi
