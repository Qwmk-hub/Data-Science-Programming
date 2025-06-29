import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('arctic.csv')

X = data[['CO2 emissions', 'temperature', 'ozone']]
y = data['glacial volume']

model = LinearRegression().fit(X, y)

y_pred = model.predict(X[-13:])
