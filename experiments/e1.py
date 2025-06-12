import glob


myfiles = glob.glob("../dati/*.txt")

print(myfiles)
for filepath in myfiles:
    with open(filepath, 'r') as file:
        content = file.read()
        print(f"Content of {filepath}:")
        print(content)
        print("-" * 40)  # Separator for readability
