import data_functions as functions
import streamlit as st

list_of_todos = functions.read_lines_file()

def add_todo():
    if "todo_key" in st.session_state:
        new_todo = st.session_state["todo_key"]
    list_of_todos.append(new_todo + "\n")
    functions.write_to_file(list_of_todos)
    st.session_state["todo_key"] = ""

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is created to increase your productivity with a minimalist approach")

for index, todo in enumerate(list_of_todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        list_of_todos.pop(index)
        functions.write_to_file(list_of_todos)
        if todo in st.session_state:
            del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="Enter a todo...",
              on_change=add_todo, key='todo_key')
