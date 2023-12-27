import pandas as pd
digits = pd.read_csv("eda.csv", header=None)
print(digits.describe())
print(digits.head(10))
print(digits.tail(10))
print(digits.sample(10))