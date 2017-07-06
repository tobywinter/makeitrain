import csv
from yahoo_finance import Share
from yahoo_finance import Currency

def get_moving_average( days ):
    with open('collated_data_without_headers.csv') as f:
        lastN = list(f)[-days:]
        print(lastN)

def get_todays_data():
    ftse = Share('^FTSE')
    ftse_price = ftse.get_open()
    gbp = Currency('GBPUSD')
    gbp_price = gbp.get_rate()
    today_data = [ftse_price, gbp_price]
    return(today_data)


def add_new_data ( today_data ):
    with open("collated_data_without_headers.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(today_data)


today_data = get_todays_data()
add_new_data(today_data)
