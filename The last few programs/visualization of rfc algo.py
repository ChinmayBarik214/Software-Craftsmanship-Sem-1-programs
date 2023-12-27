# visualizes how better or worse any model will perform when a variable is left out
# The most important variables should not be left out
# If need be, then the variable that should be removed is the one with the least importance according to this algorithm

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
iris = pd.read_csv("iris.csv")
X = iris.iloc[:,0:4]
Y = iris.iloc[:,-1]
names = iris.columns.values
rfc = RandomForestClassifier()
rfc.fit(X, Y)
importance = rfc.feature_importances_
sorted_importances = np.argsort(importance)
padding = np.arange(len(names)-1) + 0.5
plt.barh(padding, importance[sorted_importances], align='center')
plt.yticks(padding, names[sorted_importances])
plt.xlabel("Relative Importance")
plt.title("Variable Importance")
plt.show()