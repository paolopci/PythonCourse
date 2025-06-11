import csv

with open('../weather.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        print(row)  # Print each row except the header


city = input("Enter the city: ")

with open('../weather.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0].lower() == city.lower():
            print(f"Weather data for {city}:")
            print(f"Temperature: {row[1]}°C")
            break
