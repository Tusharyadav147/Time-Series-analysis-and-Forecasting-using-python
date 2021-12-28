import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("daily-min-temperatures.csv", header= 0, parse_dates=[0])
print(df.head())

df["t"] = df["Temp"].shift(1)
print(df.head())

train, test = df[1:df.shape[0]-7], df[df.shape[0]-7:]
print(train.head())

train_x, train_y = train["t"], train["Temp"]
test_x, test_y = test["t"], test["Temp"]

predictions = test_x.copy()
print(predictions)
print(test_y)

mse = mean_squared_error(test_y, predictions)
print(mse)

test_y.plot()
predictions.plot()
plt.show()
