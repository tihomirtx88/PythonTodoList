import streamlit as st
from modules.functions import get_todos, set_todos

todos = get_todos()

st.title("My Todo App");
st.subheader("This is my todo appstream");

for todo in todos:
    st.checkbox(todo);

st.text_input(label="", placeholder="Add new todo...")