import csv


with open('../weather.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Print each row of the CSV file
