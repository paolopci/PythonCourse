import FreeSimpleGUI as sg
from zip_creator import make_archive  # Importa solo la funzione make_archive

# Crea gli elementi della prima riga (selezione file)
label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
# Bottone per scegliere i file, con chiave 'files'
choose_btn1 = sg.FilesBrowse("Choose", key='files')

# Crea gli elementi della seconda riga (selezione cartella destinazione)
label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
# Bottone per scegliere la cartella, con chiave 'folder'
choose_btn2 = sg.FolderBrowse("Choose", key='folder')

# Crea il bottone di compressione
compress_btn = sg.Button('Compress')  # Bottone per avviare la compressione
# Etichetta per l'output, se necessario
output_label = sg.Text(key='output', text_color='green')

# Crea la finestra principale con il layout specificato
window = sg.Window('Files Compressor', layout=[
                   [label1, input1, choose_btn1],  # Prima riga
                   [label2, input2, choose_btn2],  # Seconda riga
                   [compress_btn, output_label]                  # Terza riga
                   ])

# Loop principale dell'applicazione
while True:
    event, values = window.read()  # Legge gli eventi e i valori dalla finestra
    print(event, values)  # Stampa gli eventi e i valori per debug
    # Elabora i dati inseriti
    # Divide i percorsi dei file usando il punto e virgola
    filepaths = values["files"].split(';')
    # Ottiene il percorso della cartella di destinazione
    folder = values['folder']
    # Chiama la funzione make_archive con i percorsi dei file e la cartella di destinazione
    make_archive(filepaths, folder)
    # Aggiorna l'etichetta di output
    window['output'].update('Files compressed successfully!')

# Chiude la finestra quando il loop termina
window.close()
