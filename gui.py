from modules import functions03
import FreeSimpleGUI as sg

layout = [
    [sg.Text("Enter a todo:")],
    [sg.InputText(tooltip="Type your todo here", key="todo"), sg.Button("Add")]
]
window = sg.Window("My To-Do App", layout=[layout], font=("Helvetica", 16))

event = window.read()

print(event)

window.close()
