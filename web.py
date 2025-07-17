import streamlit as st
from streamlit import session_state

from modules.functions import get_todos, set_todos

todos = get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n";
    todos.append(new_todo)
    set_todos(todos);

st.title("My Todo App");
st.subheader("This is my todo appstream");

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        set_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')