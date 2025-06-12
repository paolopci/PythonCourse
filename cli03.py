import os
from modules import functions03
from datetime import date
import time


now = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
print(f"Oggi è: {now}")

# print(help(load_todos))
while True:
    file_path = "dati/todos.txt"
    user_action = input(
        "Please enter a valid command (add, show, edit, complete, read, exit): "
    ).strip().lower()
# ---------------------------------------------------------------------------------
    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        with open(file_path, "a") as file:
            file.write(todo + "\n")
        print(f"Todo '{todo}' added successfully.")
# ---------------------------------------------------------------------------------
    elif user_action.startswith(("show", "list", "display")):
        os.system("cls" if os.name == "nt" else "clear")
        todos = functions03.load_todos(file_path)
        if not todos:
            print("La lista TODO è vuota.")
        else:
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item.capitalize()}")
# ---------------------------------------------------------------------------------
    elif user_action.startswith("read"):
        todos = functions03.load_todos(file_path)
        if todos:
            print("Todos loaded from file:")
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item.capitalize()}")
        else:
            print("No todos found. Please add some first.")
# ---------------------------------------------------------------------------------
    elif user_action.startswith("complete"):
        todos = functions03.load_todos(file_path)
        if not todos:
            print("No todos to complete.")
        else:
            # Mostra la lista con indici
            for i, item in enumerate(todos):
                print(f"{i+1}. {item}")
            try:
                index = int(
                    input(
                        f"Enter the index to complete (1 to {len(todos)}): ")
                )
                if 1 <= index <= len(todos):
                    completed_todo = todos.pop(index-1)
                    print(
                        f"Todo '{completed_todo}' completed and removed.")
                    functions03.save_todos(file_path, todos)
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
                continue
# ---------------------------------------------------------------------------------
    elif user_action.startswith("edit"):
        todos = functions03.load_todos(file_path)
        if not todos:
            print("No todos available to edit.")
            continue
        try:
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item}")
           # index = int(input("Enter the index of the todo to edit: "))
            index = int(user_action[5:].strip())
            if 1 <= index <= len(todos):
                new_todo = input("Enter the new todo item: ").strip()
                todos[index - 1] = new_todo
                functions03.save_todos(file_path, todos)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        continue
# ---------------------------------------------------------------------------------
    elif user_action.startswith("exit"):
        break
