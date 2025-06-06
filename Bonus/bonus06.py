contents = [
    "scrivi del testo qui "
    "per favore",
    "verifica che il testo sia corretto",
    "scrivi un testo di 1000 caratteri",
    "questo è un altro testo di esempio",
]
filenames = ["testo1.txt", "testo2.txt", "testo3.txt"]

for filename, content in zip(filenames, contents):
    with open("dati/" + filename, "w") as file:
        file.write(content)


a='paolo paci via del ' \
'canarino 5 - 61122 pesaro'
print(a)