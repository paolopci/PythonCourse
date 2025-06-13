from modules import functions03
import FreeSimpleGUI as sg

file_path = "dati/todos.txt"
# creo il layout della finestra
layout = [
    [sg.Text("Enter a todo:")],
    [sg.InputText(tooltip="Type your todo here", key="todo"),
     sg.Button("Add"), sg.Button("Exit")]
]
window = sg.Window("My To-Do App", layout=[layout], font=("Helvetica", 16))
# -------------------------------------------------
while True:
    event, values = window.read()
    print(event)  # Stampa l'evento
    print(values)  # Stampa i valori
    match event:
        case "Add":
            todos = functions03.load_todos(
                file_path)  # Load existing todos.txt
            new_todo = values['todo']
            todos.append(new_todo)  # Add new todo to the list
            functions03.save_todos(file_path, todos)
    # if event == sg.WIN_CLOSED or event == "Exit":
    #     break

window.close()
