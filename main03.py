import os


def load_todos():
    try:
        with open("dati/todos.txt", "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open("dati/todos.txt", "w") as file:
        file.write("\n".join(todos) + "\n")


while True:
    user_action = input(
        "Please enter a valid command (add, show, edit, complete, read, exit): "
    ).strip().lower()
# ---------------------------------------------------------------------------------
    if "add" in user_action:
        todo = user_action[4:].strip()
        with open("dati/todos.txt", "a") as file:
            file.write(todo + "\n")
        print(f"Todo '{todo}' added successfully.")
# ---------------------------------------------------------------------------------
    elif user_action in ("show", "list", "display"):
        os.system("cls" if os.name == "nt" else "clear")
        todos = load_todos()
        if not todos:
            print("La lista TODO è vuota.")
        else:
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item.capitalize()}")
# ---------------------------------------------------------------------------------
    elif "read" in user_action:
        todos = load_todos()
        if todos:
            print("Todos loaded from file:")
            for index, item in enumerate(todos, start=1):
                print(f"{index}. {item.capitalize()}")
        else:
            print("No todos found. Please add some first.")
# ---------------------------------------------------------------------------------
    elif "complete" in user_action:
        with open("dati/todos.txt", "r") as file:
            todos = file.read().splitlines()
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
                    with open("dati/todos.txt", "w") as file:
                        file.write("\n".join(todos) + "\n")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
# ---------------------------------------------------------------------------------
    elif 'edit' in user_action:
        todos = load_todos()
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
                save_todos(todos)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        continue
# ---------------------------------------------------------------------------------
    elif user_action == "exit":
        break
