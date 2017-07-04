import pandas_datareader.data as pdr

import datetime

import fix_yahoo_finance as yf

yf.pdr_override()

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2017, 7, 4)

ftse = pdr.get_data_yahoo("^FTSE", start, end)

ftse.to_csv('ftse.csv', encoding='utf-8')

gbp_usd = pdr.get_data_yahoo("GBPUSD=X", start, end)

gbp_usd.to_csv('gbpusd.csv', encoding='utf-8')

