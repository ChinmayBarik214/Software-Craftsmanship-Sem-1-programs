import numpy as np
import pandas as pd
values = np.array([1, None, 3, 4])
print(values)
for dtype in ['object', 'int']:
    print("dtype =", dtype)
    %timeit np.arrange(1E6, dtype=dtype).sum()