import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

df = pd.read_csv("us-airlines-monthly-aircraft-miles-flown.csv", header=0, parse_dates=[0])
print(df.head())

df["lag1"] = df["MilesMM"].shift(1)
df["MilesMM_diff_1"] = df["MilesMM"].diff(periods= 1)
print(df.head())

df.index = df["Month"]
result_a = seasonal_decompose(df["MilesMM"], model = "additive")
result_a.plot()
plt.show()

df.index = df["Month"]
result_b = seasonal_decompose(df.iloc[1:,3], model= "additive")
result_b.plot()
plt.show()

df["MilesMM"].plot()
plt.show()

df["MilesMM_diff_1"].plot()
plt.show()

df["MilesMM_diff_12"] = df["MilesMM_diff_1"].diff(periods= 12)
df["MilesMM_diff_12"].plot()
plt.show()

result_b = seasonal_decompose(df.iloc[13:,4], model="additive")
result_b.plot()
plt.show()

