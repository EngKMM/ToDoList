import functions
import time
time = time.strftime("The current time is: %d/%m/%Y %H:%M:%S")
print(time)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip().lower()
    user_action = user_action.strip()

    if user_action.startswith("add"):
        functions.add()

    elif user_action.startswith("show"):
        functions.show()

    elif user_action.startswith("complete"):
        functions.complete()

    elif user_action.startswith("edit"):
        functions.edit()

    elif user_action.startswith("exit"):
        print("Bye Bye!")
        break

    else:
        print("Please enter a valid command")
