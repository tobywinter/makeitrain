import csv
from yahoo_finance import Share
from yahoo_finance import Currency

def convert_from_CSV_to_array():
    data_array = []
    with open("collated_data_without_headers.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            data_array.append(row)
    return(data_array)

def get_moving_average( days ):
    data = convert_from_CSV_to_array()
    data_for_time_period = (data[-days:])
    total_ftse_value = 0
    for array in data_for_time_period:
        total_ftse_value += array[0]
    print(total_ftse_value/days

def get_ftse():
    ftse = Share('^FTSE')
    return(ftse.get_open())

def get_gbp():
    gbp = Currency('GBPUSD')
    return(gbp.get_rate

def get_gbp_difference():
    data = convert_from_CSV_to_array()
    data_for_time_period = data[-2:]
    two_day_gbp = data_for_time_period[0][1] + data_for_time_period[1][1]
    return(two_day_gbp/2)


def get_2day_net_price_difference():
    data = convert_from_CSV_to_array()
    data_for_time_period = data[-2:]
    two_day_price_diff = data_for_time_period[1][1] - data_for_time_period[0][1]
    return(two_day_price_diff)


def get_todays_data():
    ftse_price = get_ftse()
    gbp_price = get_gbp()
    today_data = [ftse_price, gbp_price]
    return(today_data)

def add_new_data ( today_data ):
    with open("collated_data_without_headers.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(today_data)


today_data = get_todays_data()
add_new_data(today_data)
get_gbp_difference()
