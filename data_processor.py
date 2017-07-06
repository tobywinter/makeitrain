import csv

def get_moving_average( days ):
    with open('collated_data_without_headers.csv') as f:
        lastN = list(f)[-days:]
        print(lastN)

def add_new_data ( today_data ):
    with open("collated_data_without_headers.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(row)
