import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    list_todos.append(todo+"\n")
    functions.write_todos(list_todos)

list_todos = functions.get_todos()

st.title("My ToDo App")


for index, todo in enumerate(list_todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        list_todos.pop(index)
        functions.write_todos(list_todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

st.session_state