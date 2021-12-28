import pandas as pd
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error

df = pd.read_csv("daily-min-temperatures.csv", header= 0, parse_dates=[0])
df["t"] = df["Temp"].shift(1)
df["Resid"] = df["Temp"] - df["t"]
print(df.head())

train, test = df.Resid[1:df.shape[0]-7], df.Resid[df.shape[0]-7:]
print(train.head())

model = AutoReg(train, lags=29)
model_fit = model.fit()

print(model_fit.params)

pred_resid = model_fit.predict(start=len(train), end=len(train)+len(test)-1)
predictions = df.t[df.shape[0]-7:] + pred_resid
print(predictions)

