import os


todos = []

while True:
    user_action = input(
        "Please enter a valid command (add, show, edit, exit, read o complete): "
    ).strip().lower()
    match user_action:
        case "add":
            todo = input("Enter your todo item: ").capitalize()
            todos.append(todo)
            # il file viene creato e aperto in modalità scrittura ('w') per sovrascrivere il contenuto
            with open("dati/todos.txt", "w") as file:
                file.write("\n".join(todos) + "\n")
            print(f"Todo '{todo}' added.")
        case "show" | "list" | "display":
            os.system("cls" if os.name == "nt" else "clear")
            i = 0
            for i, item in enumerate(todos, start=0):
                print(f"{i+1}. {item.title()}")
        case "read":
            # Legge i dati dal file todos.txt
            with open("dati/todos.txt", "r") as file:
                todos = file.read().splitlines()
            print("Todos loaded from file:")
            for i, item in enumerate(todos, start=1):
                print(f"{i}. {item}")
        case "edit":
            if len(todos) == 0:
                print("No todos available to edit. Please add some todos first.")
                continue
            index = int(
                input(
                    "Enter the index of the todo item to edit (1 to {}): ".format(
                        len(todos)
                    )
                )
            )
            if 1 <= index <= len(todos):
                new_todo = input("Enter the new todo item: ")
                todos[index-1] = new_todo
                print(f"Todo at index {index} updated to '{new_todo}'.")
            else:
                print("Invalid index.")
        case "complete":
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
        case "read":
            try:
                with open("dati/todos.txt", "r") as file:
                    todos = file.read().splitlines()
                    print("Todos loaded from file:")
                    for i, item in enumerate(todos, start=1):
                        print(f"{i}. {item.capitalize()}")
            except FileNotFoundError:
                print("No todos found. Please add some first.")
        case "exit":
            print("Exiting the program.")
            break
        case _:
            print(
                "Invalid command. Please type 'add', 'show', 'edit', read  or 'exit'."
            )
