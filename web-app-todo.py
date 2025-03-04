import streamlit as st
import functions as fn

todos = fn.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    fn.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for i,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=i)
    if checkbox:
        todos.pop(i)
        fn.write_todos(todos)
        del st.session_state[i]
        st.rerun()


st.text_input("", placeholder="Add your new to-do", on_change=add_todo,
              key="new_todo")
