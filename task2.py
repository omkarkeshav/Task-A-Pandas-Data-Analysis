# Task 2
# Create an account at Quandl and go here and select the below
# Hit the api (instructions in website) via python/pandas and download the data for Reliance
# Industries and save to a CSV file

import quandl
Reliance_Indust = quandl.get("BSE/BOM500325", authtoken="1P4GXUY1Ykxxmd_9-Hww")

# print(Reliance_Indust.head())

df = Reliance_Indust.iloc[::-1]
print(df)


df.to_csv('RelianceIndustriesFile.csv')
