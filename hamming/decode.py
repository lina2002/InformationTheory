import numpy

H = numpy.matrix("""0 0 0 1 1 1 1;
                    0 1 1 0 0 1 1;
                    1 0 1 0 1 0 1""")
with open('transmitted.txt', 'r') as input_file, open('decoded.txt', 'w') as output_file:
    for line in input_file:
        line = line.strip()
        x = numpy.matrix(';'.join(list(line)))
        result = H.dot(x).tolist()
        result = sum(result, [])
        result = map(lambda x: x % 2, result)
        result = ''.join(map(str, result))
        if result != '000':
            column_number = int(result, 2) - 1
            line = list(line)
            if line[column_number] == '0':
                line[column_number] = '1'
            else:
                line[column_number] = '0'
            line = ''.join(line)
        output_file.write(line)
        output_file.write('\n')
