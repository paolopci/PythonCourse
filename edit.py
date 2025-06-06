import os


todos = []

while True:
    user_action = input(
        "Please enter a valid command (add, show, edit, exit o complete): ")
    match user_action:
        case "add":
            todo = input("Enter your todo item: ").capitalize()
            todos.append(todo)
            print(f"Todo '{todo}' added.")
        case "show" | "list" | "display":
            os.system('cls' if os.name == 'nt' else 'clear')
            i = 0
            for i, item in enumerate(todos, start=0):
                print(f"{i+1}. {item.title()}")
        case "edit":
            index = int(input(
                "Enter the index of the todo item to edit (0 to {}): ".format(len(todos) - 1)))
            if 0 <= index < len(todos):
                new_todo = input("Enter the new todo item: ")
                todos[index] = new_todo
                print(f"Todo at index {index} updated to '{new_todo}'.")
            else:
                print("Invalid index.")
        case "complete":
            if not todos:
                print("No todos to complete.")
            else:
                # Mostra la lista con indici
                for i, item in enumerate(todos):
                    print(f"{i}. {item}")
                try:
                    index = int(
                        input(f"Enter the index to complete (0 to {len(todos) - 1}): "))
                    if 0 <= index < len(todos):
                        completed_todo = todos.pop(index)
                        print(
                            f"Todo '{completed_todo}' completed and removed.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Please enter a valid number.")
        case "exit":
            print("Exiting the program.")
            break
        case _:
            print("Invalid command. Please type 'add', 'show', 'edit', or 'exit'.")
