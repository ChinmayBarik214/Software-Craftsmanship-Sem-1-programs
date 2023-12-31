# Example of simple curve fitting
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#First seed the random number generator for reproducibility
np.random.seed(0)
x_data = np.linspace(-5, 5, num=50)
y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)
# And plot it
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data)
# Now fit a simple sine function to the data
def test_func(x, a, b):
    return a * np.sin(b * x)
params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2])
print(params)
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, test_func(x_data, params[0], params[1]), label='Fitted function')
plt.legend(loc='best')
plt.show()