import numpy as np
import pandas as pd
import random
digits = pd.read_csv("eda.csv", header=None)
# Take any 10 rows and make a numpy array with the indexes of those rows
randomIndex = np.array(random.sample(range(len(digits)), 10))
digitsSample = digits.iloc[randomIndex]
print(digitsSample)