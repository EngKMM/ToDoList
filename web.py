import streamlit as st
import functions


todos = functions.read_todos()


def add_todos():
    todo = st.session_state['input'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My ToDo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Enter a new ToDo...', on_change=add_todos, key='input')


