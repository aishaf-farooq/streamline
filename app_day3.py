import streamlit as st
import time 
import json
from pathlib import Path 

st.set_page_config(page_title="Course Management App", page_icon="📚", layout="wide")

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 3

tab1, tab2, tab3 = st.tabs(["View Assignment", "Add New Assignment", "Update Assignment"])



assignment = [
{
    "title": "Assignment 1",
    "due_date": "2024-07-15"
},
{
    "title": "Assignment 5",
    "due_date": "2024-08-30"
}
]

with tab3:
    st.markdown("### Update Assignment")
    st.markdown("This tab is under development. Please check back later for updates.")

    titles = []
    for assignment in assignment:
        titles.append(assignment["title"])
    selected_title = st.selectbox("Select an assignment to update", titles, key="update_assignment_selectbox")

    selected_assignment = {}
    for assignment in assignment:
        if assignment["title"] == selected_title:
            selected_assignment = assignment
            break

    edit_title = st.text_input("Edit Title", value=selected_assignment.get("title", ""), key="edit_title_input")
    edit_description = st.text_area("Edit Description", value=selected_assignment.get("description", ""), key="edit_description_textarea")
    edit_due_date = st.date_input("Edit Due Date", value=selected_assignment.get("due_date", ""), key="edit_due_date_input")

    update_btn = st.button("Update Assignment", key="update_assignment_button", use_container_width=True,type="primary", disabled=True)

    if update_btn:
        with st.spinner("Updating assignment..."):
            time.sleep(2)  # Simulate a delay for updating the assignment
        updated_assignment = {
            "title": edit_title,
            "description": edit_description,
            "due_date": str(edit_due_date)
        }

        with json_file_path.open("r", encoding="utf-8") as file:
            assignment = json.load(file)

        st.success("Assignment updated successfully in the JSON file!")
        st.dataframe(assignment)  # Display the updated assignments for verification


        # Update the assignment in the list
        for i, assignment in enumerate(assignment):
            if assignment["title"] == selected_title:
                assignment[i] = updated_assignment
                break

        # Save the updated assignments back to the JSON file
        with open(json_file_path, "w", encoding="utf-8") as file:
            json.dump(assignment, file, indent=4)

        st.success("Assignment updated successfully!")
        st.rerun()  # Refresh the app to reflect the updated assignment details





with tab1:
    st.info("This tab is under development. Please check back later for updates.")
    option = st.radio("Select an option", ["View Assignments", "Filter by Due Date", "Search by Title"])
    if option == "View Assignments":
        st.write("You selected to view all assignments.")
    elif option == "Filter by Due Date":
        st.write("You selected to filter assignments by due date.")
    elif option == "Search by Title":
        st.write("You selected to search assignments by title.")
    else:
        titles = []
        for assignment in assignments:
            titles.append(assignment["title"])
        selected_title = st.selectbox("Select an assignment to view details", options=titles)

        if not titles:
            st.warning("No assignments available to view.")
        else:
            st.write(f"You selected: {selected_title}")

            #for assignment in assignments:
                #if assignment["title"] == selected_title:
                   # with st.expander("Assignment Details", expanded=True):
                       # st.markdown(f"### Title: {assignment['title']}")
                       # st.markdown(f"**Description:** {assignment['description']}")
                        #st.markdown(f"**Due Date:** {assignment['due_date']}")  




with tab2:
    st.markdown( "### Add New Assignment")

    #input
    st.markdown("#### Assignment Title")
    title = st.text_input("Title", placeholder="Enter assignment title")
    help="Provide a brief title for the assignment, such as 'Assignment 1: Introduction to Python'."

    description = st.text_area("Description", placeholder="Enter assignment description")
    help="Provide a detailed description of the assignment, including instructions, requirements, and any relevant information for students to complete the task."



json_file_path = Path("assignments.json")

if json_file_path.exists():
    with open(json_file_path, "r", encoding="utf-8") as file:
        assignments = json.load(file)

update_btn = st.button("Save Assignment", use_container_width=True, type="primary", disabled=True)      
if update_btn:
    with st.spinner("Saving assignment..."):
        time.sleep(2)  # Simulate a delay for saving the assignment
    new_assignment = {
        "title": title,
        "description": description,
        "due_date": str(due_date)
    }

    assignments.append(new_assignment)

    with open(json_file_path, "w", encoding="utf-8") as file:f bv b
        json.dump(assignments, file, indent=4)

    st.success("Assignment saved successfully!")
    st.rerun()  # Refresh the app to reflect the new assignment details

    st.dataframe(assignments)  # Display the updated assignments for verification


for assignment in assignments:
    if assignment["title"] == title:
        with st.expander("Assignment Details", expanded=True):
            st.markdown(f"### Title: {assignment['title']}")
            st.markdown(f"**Description:** {assignment['description']}")
            st.markdown(f"**Due Date:** {assignment['due_date']}")  
        break 
    selected_title = st.selectbox("Select an assignment to view details", options=titles, key="view_assignment_selectbox")



