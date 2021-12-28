import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("daily-total-female-births-CA.csv", header=0, parse_dates=[0])
df.head()

df.index = df["date"]
#df["births"].plot()

#Zooming the plot

df1 = df[(df["date"]> "1959-01-01") & (df["date"] <= "1959-01-10")].copy()
print(df1)

df1["births"].plot()
plt.show()

#to plot trendline
sns.regplot(x= df.index.values, y = df['births'])
plt.show()