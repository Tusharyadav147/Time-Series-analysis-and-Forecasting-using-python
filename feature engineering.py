import pandas as pd

df = pd.read_csv("daily-total-female-births-CA.csv", header=0, parse_dates=[0])

features= df.copy()

features["years"] = df["date"].dt.year
features["month"] = df["date"].dt.month
features['day'] = df["date"].dt.day

features.head()

#now create lag freatures

features['lag1'] = df['births'].shift(1)
features['lag2'] = df['births'].shift(365)
features.head()

#now create window features
features["Roll_mean"] = df["births"].rolling(window=2).mean()             #create a new row in which the value is the mean of upper two value in births column
features.head()

features["Roll_max"] = df["births"].rolling(window=3).max()               #create a new column in which the value are the max value in the last 3 value from current position
features.head()

#now create expanding features
features["Expand_max"] = df["births"].expanding().max()                   #create a new column in which the value are the max value which is the max as compare to it current value
features.head(10)
