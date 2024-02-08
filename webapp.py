import streamlit as st
import Function

todos = Function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Function.write_todos(todos)


st.title("My Trajectory app")
st.write("This app is to track your daily objectives and provide your trajectory")


st.text_input(label="TASKS", placeholder="Add a task...",
              on_change=add_todo, key="new_todo")


for todo in todos:
    st.checkbox(todo)




