import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Please Enter a To-Do")
input_box = Sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = Sg.Button("Add")
listbox = Sg.Listbox(values=functions.read_todos(),
                     key="todos",
                     enable_events=True,
                     size=[45, 10])
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")

window = Sg.Window("My To-Do's",
                   layout=[[label],
                           [input_box, add_button],
                           [listbox, edit_button, complete_button]],
                   font=("Helvetica", 20))
while True:
    event, item = window.read()
    print(event)
    print(item)
    print(item['todos'])
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = item['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = item["todos"][0]
            new_todo = item["todo"]

            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete = item["todos"][0]
            todos = functions.read_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case Sg.WIN_CLOSED:
            break

