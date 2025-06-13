from modules import functions03
import FreeSimpleGUI as sg
import time


sg.theme('Black')  # Set the theme for the GUI


# Display current date and time
# now = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
# print(f"Oggi è: {now}")


file_path = "dati/todos.txt"
# Create window layout

clock = sg.Text('', key='clock')
label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors=(
    'lightblue', 'white'), tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=functions03.load_todos(file_path), key="todos", enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# -------------------------------------------------------------
# layout1 = []
# buttons_labels = ['Delete', 'Exit']
# for item in buttons_labels:
#     layout1.append(sg.Button(item))
# -------------------------------------------------------------
layout = [[clock], [label], [input_box, add_button], [
    list_box, edit_button, complete_button], [exit_button]]
# -------------------------------------------------------------
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
                todos = functions03.load_todos(file_path)
                new_todo = values['todo']
                todos.append(new_todo)
                functions03.save_todos(file_path, todos)
                window['todos'].update(values=todos)  # Update listbox
                window['todo'].update(value="")  # Clear input box

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
                    sg.popup("Please select a valid item to edit")
        case "Complete":
            try:
                # Get the first selected item
                todo_to_complete = selected[0] if selected else None
                if todo_to_complete:
                    todos = functions03.load_todos(file_path)
                    todos.remove(todo_to_complete)  # Remove the completed todo
                    functions03.save_todos(file_path, todos)
                    window['todos'].update(values=todos)  # Update listbox
                    window['todo'].update(value="")  # Clear input box
            except IndexError:
                sg.popup("Please select a todo to complete")
        case "Exit":
            print("Exiting the application")
            break
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            print("Window closed")
            break
          #  exit()

window.close()
