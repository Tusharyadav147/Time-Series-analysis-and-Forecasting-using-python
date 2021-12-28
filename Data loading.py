import pandas as pd

dataframe = pd.read_csv("daily-total-female-births-CA.csv")

print(dataframe.head())                 #to print first five row of dataframe

print(dataframe["date"].dtype)              #to check type of date column

df2 = pd.read_csv("daily-total-female-births-CA.csv", header=0, parse_dates=[0])           #to convery the date column into date formate

print(df2['date'].dtype)

print(df2.shape)               #to know how many no. of row and column we have  in our dataframe

