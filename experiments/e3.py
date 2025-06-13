import shutil

# il file zip creato si chiama output e viene creato nella cartella corrente
shutil.make_archive("output", "zip", "../dati")
# il file zip creato si chiama output e viene creato nella cartella ../dati
shutil.make_archive("../dati/output", "zip", "../dati")
