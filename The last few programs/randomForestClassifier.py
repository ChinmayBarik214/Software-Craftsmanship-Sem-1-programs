# Runs the Random Forest algorithm which can be used to find the important features
# This is used to find out how better or worse a model performs when one variable is left out.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
iris = pd.read_csv("iris.csv")
X = iris.iloc[:,0:4]
Y = iris.iloc[:,-1]
names = iris.columns.values
rfc = RandomForestClassifier()
rfc.fit(X, Y)
print("Features sorted by their score:")
print(sorted(zip(map(lambda x: round(x, 4), rfc.feature_importances_),
names), reverse=True))

# Output:
#
# Features sorted by their score:
# [(0.4706, 'Petal_length'), (0.4119, 'Petal_width'), (0.095, 'Sepal_length'), (0.0224, 'Sepal_width')]