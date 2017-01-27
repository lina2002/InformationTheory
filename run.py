import pandas

import feature_selection

file_name = input("Enter a name of input file: ")
nr_of_features = int(input("Enter a number of features to select: "))

df = pandas.read_csv(file_name)
y = df['y'].tolist()
del df['y']

indices = set()
max_value = -1
max_index = -1
for i, feature in enumerate(df):
    current = feature_selection.mutual_information([df[feature].tolist()], y)
    if current > max_value:
        max_value = current
        max_index = i
indices.add(max_index)

for _ in range(nr_of_features - 1):
    max_value = -1
    max_index = -1
    for i, feature in enumerate(df):
        if i not in indices:
            current = 0
            for idx in indices:
                current += feature_selection.mutual_information([df.iloc[:, idx].tolist(), df[feature].tolist()], y)
            if current > max_value:
                max_value = current
                max_index = i
    indices.add(max_index)

indices = list(indices)
indices.sort()

with open('output.csv', 'w') as output:
    output.write('Indices of chosen features: %s\n' % indices)
    chosen_features = []
    for i in indices:
        chosen_features.append(df.iloc[:, i].tolist())
    output.write('Mutual information: %s\n' % feature_selection.mutual_information(chosen_features, y))
