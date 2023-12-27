import pandas as pd
df = pd.read_csv("iris.csv")
print(df.query('Petal_length < Sepal_length'))