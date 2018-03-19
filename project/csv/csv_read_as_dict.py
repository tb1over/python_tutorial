import csv

with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Symbol'])