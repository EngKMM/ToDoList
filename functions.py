def read_todos(filepath='todos.txt'):
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
        return todos
    except FileNotFoundError:
        with open(filepath, 'w') as file:
            pass
        return []


def write_todos(todos_internal, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_internal)


