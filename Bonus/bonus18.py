import FreeSimpleGUI as sg


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

event, values = window.read()
window.close()  # Chiude la finestra quando il loop termina
