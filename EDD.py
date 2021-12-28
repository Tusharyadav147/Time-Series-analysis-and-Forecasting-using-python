import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("House_Price.csv", header = 0)
#print(df.head())
print(df.shape)
print(df.describe())

#to plot scattered Plot and see if we have outliers or not
sns.jointplot(x= "n_hot_rooms", y="price", data = df)
#plt.show()

sns.jointplot(x= "rainfall", y ="price", data= df)
#plt.show()

sns.jointplot(x="crime_rate", y="price", data = df)
#plt.show()

#to plot bar plot for categorical data
sns.countplot(x="airport", data = df)
#plt.show()

sns.countplot(x="waterbody", data =df)
#lt.show()

sns.countplot(x="bus_ter", data =df)
#plt.show()


#Our Observations
"""missing values in n_hos_beds
skewness or outliers in crime rate
Outliers in n_hot_rooms and rainfall
bus_ter has only "Yes" values"""


#here we remove the outliers
print(df.info())

print(np.percentile(df.n_hot_rooms,[99]))
uv = np.percentile(df.n_hot_rooms,[99])[0]
print(df[(df.n_hot_rooms > uv)])
df.n_hot_rooms[(df.n_hot_rooms > 3*uv)] = 3*uv

print(np.percentile(df.rainfall,[1])[0])
lv = np.percentile(df.rainfall,[1])[0]
print(df[(df.rainfall < lv)])
df.rainfall[(df.rainfall < .3*lv)] = 3*lv

#dealing with missing values
df.n_hos_beds = df.n_hos_beds.fillna(df.n_hos_beds.mean())
print(df.info())