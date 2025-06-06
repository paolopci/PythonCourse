user_prompt = "Enter your todo item: "
nvolte = 1
todos = []
while nvolte < 5:
    todo = input(user_prompt).capitalize()
    todos.append(todo)
    nvolte += 1
print(todos)
