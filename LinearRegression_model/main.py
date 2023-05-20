import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, 0]
y = dataset.iloc[:, 1]
# print(X)
# print(y)

# No missing data
#
# No Categorical data
#
# Split dataset into training and test sets

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)
#
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# Train the model

from sklearn.linear_model import LinearRegression

regressor = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)
regressor.fit(x_train, y_train)

# Predict Test Set result
y_pred = regressor.predict(x_test)

# Visualize training set results
plt.scatter(x=x_train, y=y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs. Experience (Training Set)')
plt.xlabel('Experience (yrs)')
plt.xlabel('Salary ($/year)')
plt.show()

# Visualize test set results
plt.scatter(x=x_test, y=y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs. Experience (Test Set)')
plt.xlabel('Experience (yrs)')
plt.xlabel('Salary ($/year)')
plt.show()
