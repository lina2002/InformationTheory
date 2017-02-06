import numpy

G = numpy.matrix("""1 0 0 0;
                    0 1 0 0;
                    0 0 1 0;
                    0 0 0 1;
                    0 1 1 1;
                    1 0 1 1;
                    1 1 0 1""")
with open('original.txt', 'r') as input_file, open('encoded.txt', 'w') as output_file:
    for line in input_file:
        line = line.strip()
        x = numpy.matrix(';'.join(list(line)))
        result = G.dot(x).tolist()
        result = sum(result, [])
        result = map(lambda x: x % 2, result)
        output_file.write(''.join(map(str, result)))
        output_file.write('\n')
