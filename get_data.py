import pandas as pd
import pandas_datareader as pdr
from datetime import datetime, timedelta

def get_ftse(start_date, end_date):
    ftse = pdr.get_data_yahoo('^FTSE', start_date, end_date)
    ftse.to_csv('ftse.csv', columns=['Adj Close', 'Volume'], encoding='utf-8')

def get_gbp_usd(start_date, end_date):
    gbp_usd = pdr.get_data_yahoo('GBPUSD=X', start_date, end_date)
    gbp_usd.to_csv('gbp_usd.csv', columns=['Adj Close'], encoding='utf-8')

def merge_data(ftse_csv, gbp_csv):

    ftse = pd.read_csv(ftse_csv,
            header=0,
            index_col=["Date"],
            parse_dates=["Date"])

    ftse.rename(columns=lambda x: 'ftse_' + x, inplace=True)

    gbp_usd = pd.read_csv(gbp_csv,
            header=0,
            index_col=["Date"],
            parse_dates=["Date"],
            )

    gbp_usd.rename(columns=lambda x: 'gbusd_' + x, inplace=True)

    merged = pd.concat([ftse, gbp_usd], axis=1, join_axes=[gbp_usd.index])
    merged = merged.ffill()
    merged.to_csv('merged.csv', encoding='utf-8')

def get_data():
    yesterday = datetime.today() - timedelta(1)
    one_month_ago = yesterday - timedelta(days=50)
    get_ftse(one_month_ago , yesterday)
    get_gbp_usd(one_month_ago, yesterday)
    merge_data('ftse.csv', 'gbp_usd.csv')

if __name__ == '__main__':
    yesterday = datetime.today() - timedelta(1)
    one_month_ago = yesterday - timedelta(days=50)
    get_ftse(one_month_ago , yesterday)
    get_gbp_usd(one_month_ago, yesterday)
    merge_data('ftse.csv', 'gbp_usd.csv')
