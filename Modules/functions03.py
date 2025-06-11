

def load_todos(file_path):
    """ Load todos from a file, returning a list of todos. """
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_todos(file_path, todos):
    """ Save todos to a file. """
    with open(file_path, "w") as file:
        file.write("\n".join(todos) + "\n")


print(__name__)

if __name__ == "__main__":
    print('Hello from functions03.py!')
    print(load_todos())
