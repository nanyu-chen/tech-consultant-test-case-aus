import pandas as pd
from datetime import datetime

df = pd.read_excel('part-2/data.xlsx')

df['Time'] = pd.to_datetime(df['time'])

df.set_index('Time', inplace=True)

sales_per_15min = df.resample('15min').agg({'sales': ['sum', 'count']})
sales_per_15min.columns = ['Sales', 'Transactions']

sales_per_15min.reset_index(inplace=True)

sales_per_15min.to_csv('part-2/sales_per_15min_pandas.csv', index=False)