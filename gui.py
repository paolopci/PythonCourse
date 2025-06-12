from modules import functions03
import FreeSimpleGUI as sg

layout = [
    [sg.Text("Enter a todo:")],
    [sg.InputText(tooltip="Type your todo here"), sg.Button("Add")]
]
window = sg.Window("My To-Do App", layout=[layout])

window.read()

print('Ciao Paolo .....')

window.close()
