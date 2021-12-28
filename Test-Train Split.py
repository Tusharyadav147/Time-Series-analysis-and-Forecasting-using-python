import pandas as pd
import numpy as np

df = pd.read_csv("daily-min-temperatures.csv", header = 0, parse_dates=[0])
print(df.head())          #print the first five dataset
print(df.tail())          #print the last five dataset
print(df.shape)           #print the shape of dataset
print(df.shape[0])        #to see the number of records in myfirst column
train_size = int(df.shape[0]*.8)        #to find how many no. of rows we require to use 80% of dataset
print(train_size)

train = df[0:train_size]
print(train.shape)

test = df[train_size:]
print(test.shape)
