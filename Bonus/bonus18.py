import FreeSimpleGUI as sg
# Importa la funzione di estrazione dal file zip_extractor.py
from zip_extractor import extract_zip


# Crea gli elementi della prima riga (selezione file)
label1 = sg.Text('Select archive:')
input1 = sg.Input()
# posso selezionare un SOLO file, non più multipli
choose_btn1 = sg.FileBrowse("Choose", key='archive')


# Crea gli elementi della seconda riga (selezione cartella destinazione)
label2 = sg.Text('Select dest dir:')
input2 = sg.Input()
# Bottone per scegliere la cartella, con chiave 'folder'
choose_btn2 = sg.FolderBrowse("Choose", key='folder')

# Crea il bottone di compressione
extract_btn = sg.Button('Extract')  # Bottone per avviare la compressione
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('Files Compressor', layout=[
                   [label1, input1, choose_btn1],  # Prima riga
                   [label2, input2, choose_btn2],  # Seconda riga
                   [extract_btn, output_label]                  # Terza riga
                   ])

while True:
    event, values = window.read()
    print(event, values)  # Stampa l'evento e i valori per il debug
    archivepath = values['archive']  # Percorso dell'archivio selezionato
    dest_path = values['folder']  # Percorso della cartella di destinazione
    print(archivepath)
    print(dest_path)

    extract_zip(archivepath, dest_path)  # Chiama la funzione di estrazione
    # Aggiorna l'etichetta di output
    window['output'].update('Extraction complete!')


window.close()  # Chiude la finestra quando il loop termina
