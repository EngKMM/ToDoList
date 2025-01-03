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


def add():
    todo = user_action[4:].strip()

    if not todo:
        print("cannot add empty todo")
        return

    todos = read_todos("todos.txt")
    todos.append(todo + "\n")

    write_todos(todos)
    print(f"{todo} was added")


def show():
    todos = read_todos("todos.txt")
    new_todos = [item.strip("\n") for item in todos]

    for index, item in enumerate(new_todos):
        row = f"{index + 1}-{item}"
        print(row)
    if not todos:
        print("No todos found.")
        return


def complete():

    try:
        number = int(user_action[9:])
        todos = read_todos("todos.txt")

        index = number - 1
        removed_todo = todos[index].strip("\n")
        todos.pop(index)

        write_todos(todos)
        print(f"{removed_todo} was Completed")

    except IndexError:
        print("The number you entered is out of range")
    except ValueError:
        print("Please input a valid todo index")


def edit():
    try:
        todos = read_todos("todos.txt")

        number = int(user_action[5:])
        index = number - 1
        old_todo = todos[index].strip("\n")

        new_todo = input("Enter a new todo: ") + "\n"
        todos[index] = new_todo

        write_todos(todos)

        print(f"{old_todo} was replaced with {new_todo}")

    except ValueError:
        print("Please input a valid list-item number")
    except IndexError:
        print("This index number is out of range please input a valid number")
