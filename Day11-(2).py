import csv

def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)

        next(reader)      # Skip header

        for row in reader:
            yield row


for record in read_csv("students.csv"):
    print(record)