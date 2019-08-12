import csv

<<<<<<< HEAD
with open("demo.csv", newline="") as csv_file:
=======
with open("./demo.csv", newline="") as csv_file:
>>>>>>> a617cdac10fab618e132cf6eaea05fc1ea992265
    csv_data = csv.reader(csv_file, delimiter=",")
    for row in csv_data:
        try:
            data_row = row[0]
            print(data_row)
        except IndexError:
            exit()
