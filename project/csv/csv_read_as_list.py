import csv

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)

    for row in f_csv:
        print(row)