from modules import functions03
import FreeSimpleGUI as sg
import time
import sys
import os


def get_todos_path():
    """Crea il file todos.txt nella sottocartella 'dati' relativa all'eseguibile"""

    try:
        # Ottieni la directory dell'eseguibile
        if getattr(sys, 'frozen', False):
            # Se è un eseguibile PyInstaller
            exe_dir = os.path.dirname(sys.executable)
        else:
            # Se è uno script Python normale
            exe_dir = os.path.dirname(os.path.abspath(__file__))

        # Crea la cartella 'dati' nella stessa directory dell'eseguibile
        data_dir = os.path.join(exe_dir, "dati")

        # Crea la directory 'dati' se non esiste
        os.makedirs(data_dir, exist_ok=True)
        print(f"Directory dati creata/verificata: {data_dir}")

        # Percorso completo del file todos.txt
        todos_path = os.path.join(data_dir, "todos.txt")

        # Se il file non esiste, crealo vuoto
        if not os.path.exists(todos_path):
            with open(todos_path, 'w', encoding='utf-8') as f:
                f.write("")
            print(f"Creato file todos: {todos_path}")

        print(f"File todos: {todos_path}")
        return todos_path

    except Exception as e:
        print(f"Errore nella creazione del percorso dati: {e}")
        # Fallback: usa la directory corrente
        fallback_dir = os.path.join(os.getcwd(), "dati")
        os.makedirs(fallback_dir, exist_ok=True)
        fallback_path = os.path.join(fallback_dir, "todos.txt")

        if not os.path.exists(fallback_path):
            with open(fallback_path, 'w', encoding='utf-8') as f:
                f.write("")

        print(f"Usando percorso fallback: {fallback_path}")
        return fallback_path


sg.theme('Black')  # Set the theme for the GUI

# File todos nella sottocartella 'dati' relativa all'eseguibile
try:
    file_path = get_todos_path()
except Exception as e:
    sg.popup_error(f"Errore nell'inizializzazione del file: {str(e)}")
    sys.exit(1)

# Create window layout
clock = sg.Text('', key='clock')
label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="enter todo", key="todo")

add_button = sg.Button("Add", size=(10, 1),
                       mouseover_colors='LightBlue2',
                       tooltip="Add todo", key="Add")

# Carica i todos esistenti in modo sicuro
try:
    initial_todos = functions03.load_todos(file_path)
except Exception as e:
    print(f"Errore nel caricamento todos: {e}")
    initial_todos = []

list_box = sg.Listbox(values=initial_todos, key="todos", enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Aggiungi un testo che mostra dove è salvato il file
file_info = sg.Text(f"File salvato in: {file_path}", font=(
    "Helvetica", 8), text_color="gray")

layout = [[clock], [label], [input_box, add_button], [
    list_box, edit_button, complete_button], [file_info], [exit_button]]

# create the window
window = sg.Window(
    "My To-Do App", layout=layout, font=("Helvetica", 16))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(time.strftime('%d %b %Y %H:%M:%S'))  # Update clock
    print("Event:", event)  # Print event
    print("Values:", values)  # Print selected items

    # Safely print selected items
    selected = values.get('todos', []) if values else []
    print("Selected:", selected)

    match event:
        case "Add":
            if values.get('todo'):  # Check if input is not empty
                try:
                    todos = functions03.load_todos(file_path)
                    new_todo = values['todo']
                    todos.append(new_todo)
                    functions03.save_todos(file_path, todos)
                    window['todos'].update(values=todos)  # Update listbox
                    window['todo'].update(value="")  # Clear input box
                except Exception as e:
                    sg.popup_error(f"Errore nel salvare: {str(e)}")

        case "Edit":
            todos = values.get('todos', [])
            # Check if item is selected and input is not empty
            if todos and values.get('todo'):
                try:
                    todo_to_edit = todos[0]
                    new_todo = values['todo']
                    todos = functions03.load_todos(file_path)
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions03.save_todos(file_path, todos)
                    window['todos'].update(values=todos)  # Update listbox
                    window['todo'].update(value="")  # Clear input box
                except (ValueError, IndexError):
                    sg.popup_error("Please select a valid item to edit")
                except Exception as e:
                    sg.popup_error(f"Errore nell'editing: {str(e)}")

        case "Complete":
            todos = values.get('todos', [])
            if todos:
                try:
                    todo_to_complete = todos[0]
                    todos = functions03.load_todos(file_path)
                    todos.remove(todo_to_complete)
                    functions03.save_todos(file_path, todos)
                    window['todos'].update(values=todos)  # Update listbox
                except (ValueError, IndexError):
                    sg.popup_error("Please select a valid item to complete")
                except Exception as e:
                    sg.popup_error(f"Errore nel completare: {str(e)}")

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
