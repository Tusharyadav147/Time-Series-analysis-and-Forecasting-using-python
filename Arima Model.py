import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima_model import ARIMA

df = pd.read_csv("shampoo.csv", header = 0, parse_dates=[0])
print(df.head())

#to find the value of D first plot the line graph and see the trend i.e. its exponantial or not
df["Sales"].plot()
plt.show()

#to find the value of P plot autocorrelation plot and see where the graph cut the confience interval line
autocorrelation_plot(df["Sales"])
plt.show()

#to find the value of Q plot partial autocorrelation  plot and see where the graph cut the trend
plot_pacf(df["Sales"], lags=15)

#now make the arima model
model = ARIMA(df["Sales"], order= (2,2,5))
model_fit = model.fit()
print(model_fit.summary())
residuals = model_fit.resid
residuals.plot()
plt.show()
residuals.describle()

output = model_fit.forecast()
print(output)
