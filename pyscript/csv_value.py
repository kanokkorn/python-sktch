import csv

with open("./demo.csv", newline="") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    for row in csv_data:
        try:
            data_row = row[0]
            print(data_row)
        except IndexError:
            exit()
