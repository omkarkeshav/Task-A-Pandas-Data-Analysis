# Task 1a
# Included is the file containing a time-series data from the stock market. For every stock
# mentioned, we have data for several days at a 60Mins frequency containing the Open, High,
# Low and Close Values.
# Convert/Resample 60Mins data into 1day candles data

import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)


df = pd.read_csv(r"D:\omkar\\Spot_60Min_50Stocks.csv")
# print(df.head(10))

df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)
# print(df.head(10))

df['TS1'] = pd.to_datetime(df['TS1'])
df.set_index('TS1', inplace=True)
# print(df.head(10))

# Showing open high low close values
# data = df['VOL'].resample('1D').ohlc()
# data.dropna(inplace=True)
# print(data)

# showing open high low close vol values
df = df.groupby('SYMBOL').resample('D').agg({'OPEN': 'first', 'HIGH': 'max', 'LOW': 'min', 'CLOSE': 'last', 'VOL': 'sum'})
df.dropna(inplace=True)
print(df)
# print(df.head(10))
df.to_csv('1d_resample.csv')
