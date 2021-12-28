import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

df = pd.read_csv("daily-total-female-births-CA.csv", header=0, parse_dates=[0])
print(df.head())

df.index = df["date"]
print(df.head())

result = seasonal_decompose(df["births"], model = "additive")
result.plot()
plt.show()

result2 = seasonal_decompose(df["births"], model="multiplicative")
result2.plot()
plt.show()

