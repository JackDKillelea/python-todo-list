import data_functions as functions
import streamlit as st

list_of_todos = functions.read_lines_file()

def add_todo():
    if "todo_key" in st.session_state:
        new_todo = st.session_state["todo_key"]
    list_of_todos.append(new_todo + "\n")
    functions.write_to_file(list_of_todos)
    st.session_state["todo_key"] = ""

st.title("Minimalist Global Todo List")
st.subheader("This is a todo list that is shared globally.")
st.write("Please feel free to test the todo list app by adding and completing todos")

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
