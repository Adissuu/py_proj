import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import dataset
dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
# print(X)
# print(y)

# No missing data
#
# Categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array((ct.fit_transform(X)))

# Split dataset into training and test sets

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

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
np.set_printoptions(precision=2)

print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.values.reshape(len(y_test), 1)), 1))


