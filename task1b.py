# Task 1b
# Calculate 13 period rolling/moving average of High and 5 rolling/period moving average of close
# for every Symbol.
# If Moving Average of close crosses Moving Average of High from below mark that as a "flag" (1)
# Identify all the stocks for the last 5 days which had a flag in it.
# Attempt to do this with pandas, using functions(if possible).

import pandas as pd
import numpy as np
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv(r"D:\omkar\\1d_resample.csv")
# print(df.head(10))

# Calculate 13 period rolling/moving average of High
df['13p_rollingAvg'] = df.groupby('SYMBOL', sort=False).rolling(window=13).HIGH.mean().reset_index(drop='SYMBOL')
# print(df)

# 5 rolling/period moving average of close
df['5Close_rollingAvg'] = df.groupby('SYMBOL', sort=False).rolling(window=5).CLOSE.mean().reset_index(drop='SYMBOL')
# print(df.head(10))

# If Moving Average of close crosses Moving Average of High from below mark that as a "flag" (1)
df['FLAG'] = np.where(df['5Close_rollingAvg'] > df['13p_rollingAvg'], 1, 0)
# print(df.head(20))

# Identify all the stocks for the last 5 days which had a flag in it.
df.groupby('SYMBOL').tail(5)
# print(df)

# all the stocks for the last 5 days which had a flag in it.


def lst_5day(df):
    Name_of_Shares = []
    new_data = df.groupby('SYMBOL').tail(5)
    new_data.set_index('SYMBOL', inplace=True)
    indexNames = new_data[new_data['FLAG'] == 1].index
    indexNames = list(set(indexNames))
    return indexNames


print(lst_5day(df))
