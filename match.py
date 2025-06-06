todos = []
stato = True

while stato:
    user_action = input("Type add, show o exit > ")
    user_action = user_action.strip().lower()
    match user_action:
        case "add":
            todo = input("Enter your todo item: ").capitalize()
            todos.append(todo)
         #   print(f"Todo '{todo}' added.")
        case "show" | "list" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            print("Exiting the program.")
            stato = False
        case _:
            print("Invalid command. Please type 'add', 'show', or 'exit'.")
