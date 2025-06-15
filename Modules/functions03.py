import os


def load_todos(file_path):
    """Carica i todos dal file, restituisce lista vuota se il file non esiste"""
    try:
        # Assicurati che la directory esista
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Se il file non esiste, crealo vuoto
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("")
            return []

        # Leggi il file
        with open(file_path, 'r', encoding='utf-8') as f:
            todos = f.readlines()

        # Rimuovi i caratteri di nuova riga e spazi extra
        todos = [todo.strip() for todo in todos if todo.strip()]
        return todos

    except Exception as e:
        print(f"Errore nel caricamento dei todos: {e}")
        return []


def save_todos(file_path, todos):
    """Salva i todos nel file"""
    try:
        # Assicurati che la directory esista
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Salva i todos
        with open(file_path, 'w', encoding='utf-8') as f:
            for todo in todos:
                f.write(todo + '\n')

    except Exception as e:
        print(f"Errore nel salvataggio dei todos: {e}")
        raise  # Rilancia l'eccezione per farla gestire dal GUI
