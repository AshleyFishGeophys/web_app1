import streamlit as st
from modules.functions import *


FILEPATH = "files/todos.txt"

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos, FILEPATH)


todos = get_todos(FILEPATH)

st.title("My Honey-Do List App")
# st.subheader("This is my todo app.")
st.write("This app is to help you keep track of your Honey-Do items!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos, FILEPATH)
        del st.session_state[todo]
        # st.rerun()
        st.experimental_rerun()

st.text_input(
    label="Enter a todo: ",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo")

print("Hello")  # prints in the terminal, not in the web app

# The session_state will show everything that has keys
st.session_state