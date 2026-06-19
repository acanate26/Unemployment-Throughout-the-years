print("Unemployment Rates in the United States")
##We will be analyzing unemployment between men and women's ages, years, race, and education levels from the year 1948 to 2024.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import col
education = pd.read_csv('education_usa.csv')
unemp_data = pd.read_csv('unemployment_data_us.csv')
unemp_sex = pd.read_csv('df_sex_unemployment_rates.csv')

for name, df in [("Education", education), ("Unemployment Data", unemp_data), ("Unemployment by Sex", unemp_sex)]:
     print(f"\n=== {name} ===")
     print(df.shape)
     print(df.dtypes)
     print(df.head(3))
     print(df.describe())
     print(df.isnull().sum())


#Plotting Unemployment by Education Level
unemp_data.groupby("Year")[["Primary_School", "High_School", "Associates_Degree", "Professional_Degree"]].mean().plot(title="Unemployment by Education Level")
plt.show()

#Plotting Uemployment by Sex
unemp_sex.plot(x='date', y=['men_rate', 'women_rate'], title='Unemployment Rates by Sex')
plt.show()

#Plotting Unemployment by Race 
unemp_data.groupby("Year")[["White", "Black", "Asian", "Hispanic"]].mean().plot(title="Unemployment by Race")
plt.show()

#Plottting Race and Sex side by side 
df_annual = unemp_data.groupby("Year")[["White", "Black", "Asian", "Hispanic", "Men", "Women"]].mean()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
df_annual[["White", "Black", "Asian", "Hispanic"]].plot(ax=ax1, marker='o', title="Unemployment by Race")
df_annual[["Men", "Women"]].plot(ax=ax2, marker='o', title="Unemployment by Sex")
ax1.set_ylabel("Unemployment Rate (%)")
ax2.set_ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()



