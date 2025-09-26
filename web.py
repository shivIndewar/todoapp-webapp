import streamlit as st
from streamlit import session_state

import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"]= ""


st.title("Todo App Using Streamlit")
st.subheader("This is the web based todo app")
st.write("This app will help you out to manage your tasks")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="What do you want to do?", placeholder="Enter your task", on_change=add_todo, key="new_todo")
