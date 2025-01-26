import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Please Enter a To-Do")
input_box = Sg.InputText(tooltip="Enter To-Do", key = "todo")
button = Sg.Button("Add")

window = Sg.Window("My To-Do's",
                   layout=[[label], [input_box, button]],
                   font=("Helvetica", 20))
while True:
    event, item = window.read()
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = item['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break
