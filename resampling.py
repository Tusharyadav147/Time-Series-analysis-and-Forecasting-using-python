import pandas as pd

df = pd.read_csv("daily-total-female-births-CA.csv", header=0, parse_dates=[0])
df.head()

#downsampling

quarterly_birth_df = df.resample("Q", on= "date").mean()       #to change the data quarterly
quarterly_birth_df.head()

yearly_total_birth_df = df.resample("A", on="date").sum()
yearly_total_birth_df.head()

#upsampling

upsampling_birth_df = df.resample("D", on = "date").mean()
print(upsampling_birth_df)