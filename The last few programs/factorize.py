# Assign a number to each unique value in the column 'Class' starting from 0 then 1 then 2 and so on then,
# replace the string there with the value assigned to it and
# in labels put
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]
# in uniques put
# Index(['Setosa', 'Versicolor', 'Virginica'], dtype='object')

import pandas as pd
df = pd.read_csv("iris.csv")
# Factorize the values
labels, uniques = pd.factorize(df['Class'])
# Save the encoded variables in “iris.Class”
df['Class'] = labels
# Print out the first rows
print(df['Class'].head(100))
# print(labels)
# print(uniques)
