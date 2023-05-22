import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
# print(X)
# print(y)

# No missing data
#
# No Categorical data
#

# Split dataset into training and test sets


# Train the linear model

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
# Training polynomial on the dataset
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualizing the linear regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Salary vs Level and Position (Linear Regression)')
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# Visualizing the polynomial regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Salary vs Level and Position (Polynomial Regression)')
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

# Predict new result with linear regression
print(lin_reg.predict([[6.5]]))
# Predict new result with polynomial regression
print(lin_reg_2.predict(poly_reg.fit_transform([[6.5]])))
