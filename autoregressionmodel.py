import numpy as np
import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

"""# load dataset
df = pd.read_csv('daily-min-temperatures.csv', header=0, parse_dates=[0])
print(df.head())

# split dataset
train, test = df.Temp[1:df.shape[0]-7], df.Temp[df.shape[0]-7:]
print(train.head())

# train autoregression
model = AutoReg(train, lags=29)
model_fit = model.fit()
print('Coefficients: %s' % model_fit.params)

# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1)
for i in range(len(predictions)):
	print('predicted={}, expected={}'.format(predictions[i], test[i]))
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)

# plot results
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()"""


df = pd.read_csv("daily-min-temperatures.csv", header=0, parse_dates=[0])
train, test = df.Temp[1:df.shape[0]-7], df.Temp[df.shape[0]-7:]

data = train
predict = []
for t in test:
    model = AutoReg(data,lags=29)
    model_fit = model.fit()
    y = model_fit.predict(start= len(data), end= len(train)+len(test)-1)
    print(y.value[0])
    predict.append(y.value[0])
    data = np.append(data, t)
    data = pd.Series(data)
