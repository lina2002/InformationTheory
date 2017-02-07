with open('original.txt', 'r') as original, open('decoded.txt', 'r') as decoded:
    same = 0
    different = 0
    original_lines = list(original)
    decoded_lines = list(decoded)
    for (original_line, decoded_line) in zip(original_lines, decoded_lines):
        if decoded_line.startswith(original_line.strip()):
            same += 1
        else:
            different += 1
print(same)
print(different)