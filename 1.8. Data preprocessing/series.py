import pandas as pd
import numpy as np
data = pd.Series([1, np.nan, 2, None])
print(data)
print(data.values)
print(data.index)
print(data[1])
print(data[1:3])