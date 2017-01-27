import itertools
import math


def mutual_information(x, y):
    n = len(x) + 1
    xy = list(x)
    xy.append(y)
    xy = list(zip(*xy))
    x = list(zip(*x))
    l = len(y)
    mi = 0
    binary_sequences = list(itertools.product([0, 1], repeat=n))
    for binary_sequence in binary_sequences:
        if xy.count(binary_sequence):
            mi += (xy.count(binary_sequence) / l) * \
                  math.log2((xy.count(binary_sequence) * l) / (x.count(binary_sequence[:-1]) * y.count(binary_sequence[-1])))
    return mi
