import streamlit as st

#Store Task in session
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("✅ To-Do List App")

# User input
new_task = st.text_input("Enter your task")

# Add task
if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})

# Tasks list 
st.subheader("Your Tasks")

if not st.session_state.tasks:
    st.write("🎉 No tasks yet! Add a new one above.")
else:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        
        # Checkbox to complete and uncomplate task
        done = col1.checkbox("", task["done"], key=f"task_{i}")
        st.session_state.tasks[i]["done"] = done

        # Show task (completed to strike-through style)
        col2.markdown(f"~~{task['task']}~~" if done else task["task"])

        # Delete button
        if col3.button("❌", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
