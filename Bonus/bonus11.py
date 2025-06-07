def get_avarange():
    with open('../dati/data.txt', 'r') as file:
        data = file.readlines()
        numbers = [float(line.strip())
                   for line in data if line.strip().replace('.', '', 1).isdigit()]
        if numbers:
            return sum(numbers) / len(numbers)
        else:
            return 0


avarange = get_avarange()
print(avarange)
