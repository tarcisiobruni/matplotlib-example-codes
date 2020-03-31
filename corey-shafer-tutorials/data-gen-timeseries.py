import csv
import random
import time
from datetime import datetime, timedelta

date_value = datetime(2015,1,1)
number_value = 50

# csv header
fieldnames = ["date_value", "number_value"]

with open('data-live-time-series.g.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data-live-time-series.g.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "date_value": date_value.strftime("%Y-%m-%d"),
            "number_value": number_value
        }

        csv_writer.writerow(info)
        print(date_value.strftime("%Y-%m-%d"), number_value)

        date_value += timedelta(1)
        number_value = round(random.uniform(number_value-4 if number_value-4 >=0 else number_value, number_value+4 if number_value+4 <=100 else number_value),2) \
                        if (number_value>=0 and number_value <= 100 ) else number_value

    time.sleep(0.125)