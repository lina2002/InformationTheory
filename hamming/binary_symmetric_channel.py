import random

p = float(input('Enter the probability of error: '))

with open('encoded.txt', 'r') as input_file, open('transmitted.txt', 'w') as output_file:
    for line in input_file:
        for symbol in line:
            if symbol == '\n':
                continue
            zero = symbol == '0'
            if random.random() <= p:
                zero = not zero
            if zero:
                output_file.write('0')
            else:
                output_file.write('1')
        output_file.write('\n')
