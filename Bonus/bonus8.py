from datetime import date

data_oggi = date.today()
data_italiana = data_oggi.strftime("%d-%m-%Y")
print(data_italiana)  # Output: 05-06-2025

# -----------------
mood = input('come stai oggi from 1 to 10? ')

journal = input('scrivi il tuo diario: ')


with open(f'../journal/{data_italiana}.txt', 'w') as file:
    file.write(mood + '\n')
    file.write(journal)
