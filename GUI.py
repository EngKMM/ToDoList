import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Please Enter a To-Do")
input_box = Sg.InputText(tooltip="Enter To-Do")
button = Sg.Button("Add")

window = Sg.Window("My To-Do's", layout=[[label], [input_box, button]])
window.read()
