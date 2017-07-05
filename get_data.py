import pandas as pd
import pandas_datareader.data as pdr
import datetime
import fix_yahoo_finance as yf

#yf.pdr_override()
#
#start = datetime.datetime(2010, 1, 1)
#
#end = datetime.datetime(2017, 7, 4)
#
#ftse = pdr.get_data_yahoo("^FTSE", start, end)
#
#print(ftse)
#
#ftse.to_csv('ftse.csv', encoding='utf-8')
#
#gbp_usd = pdr.get_data_yahoo("GBPUSD=X", start, end)
#
#gbp_usd.to_csv('gbpusd.csv', encoding='utf-8')


ftse = pd.read_csv('ftse.csv',
        header=0,
        index_col=["Date"],
        parse_dates=["Date"])

ftse.rename(columns=lambda x: 'ftse_' + x, inplace=True)


gbp_usd = pd.read_csv('gbpusd.csv',
        header=0,
        index_col=["Date"],
        parse_dates=["Date"],
        )

gbp_usd.rename(columns=lambda x: 'gbusd_' + x, inplace=True)

#print(gbp_usd.shape)
# print(ftse.shape)
result = pd.concat([ftse, gbp_usd], axis=1, join_axes=[gbp_usd.index])

print(result.shape)
