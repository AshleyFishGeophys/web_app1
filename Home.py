import streamlit as st
from functions import *


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos, FILEPATH)


st.set_page_config(layout="wide")

todos = get_todos()

st.title("My Honey-Do List App")
# st.subheader("This is my todo app.")
st.write("This app is to help you keep track of your Honey-Do <b><i>'requests'</i></b>!",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        # st.rerun()
        st.experimental_rerun()

st.text_input(
    label="Enter a todo: ",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo")
