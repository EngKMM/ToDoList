import functions
import time
time = time.strftime("The current time is: %d/%m/%Y %H:%M:%S")
print(time)
# Anas
def add():
    todo = user_action[4:].strip()

    if not todo:
        print("cannot add empty todo")
        return

    todos = functions.read_todos("todos.txt")
    todos.append(todo + "\n")

    functions.write_todos(todos)
    print(f"{todo} was added")


def show():
    todos = functions.read_todos("todos.txt")
    new_todos = [item.strip("\n") for item in todos]

    for index, item in enumerate(new_todos):
        row = f"{index + 1}-{item}"
        print(row)
    if not todos:
        print("No todos found.")
        return

# ABDULLAH
def complete():

    try:
        number = int(user_action[9:])
        todos = functions.read_todos("todos.txt")

        index = number - 1
        removed_todo = todos[index].strip("\n")
        todos.pop(index)

        functions.write_todos(todos)
        print(f"{removed_todo} was Completed")

    except IndexError:
        print("The number you entered is out of range")
    except ValueError:
        print("Please input a valid todo index")


def edit():
    try:
        todos = functions.read_todos("todos.txt")

        number = int(user_action[5:])
        index = number - 1
        old_todo = todos[index].strip("\n")

        new_todo = input("Enter a new todo: ") + "\n"
        todos[index] = new_todo

        functions.write_todos(todos)

        print(f"{old_todo} was replaced with {new_todo}")

    except ValueError:
        print("Please input a valid list-item number")
    except IndexError:
        print("This index number is out of range please input a valid number")


while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        add()

    elif user_action.startswith("show"):
        show()

    elif user_action.startswith("complete"):
        complete()

    elif user_action.startswith("edit"):
        edit()

    elif user_action.startswith("exit"):
        print("Bye Bye!")
        break

    else:
        print("Please enter a valid command")
