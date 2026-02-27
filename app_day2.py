import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 3

st.write("---")

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

#Add new assignment
st.markdown( "### Add New Assignment")

#input
st.markdown("#### Assignment Title")
title = st.text_input("Title", placeholder="Enter assignment title")
help="Provide a brief title for the assignment, such as 'Assignment 1: Introduction to Python'."

description = st.text_area("Description", placeholder="Enter assignment description")
help="Provide a detailed description of the assignment, including instructions, requirements, and any relevant information for students to complete the task."

st.markdown("#### Due Date")
due_date = st.date_input("Due Date")
help="Select the due date for the assignment. This will help students manage their time and ensure they submit their work on time."
assignments_type = st.radio("Assignment Type", options=["Homework", "Project", "Quiz"], help="Choose the type of assignment to categorize it appropriately.")
assignments_type2= st.selectbox("Assignment Type", options=["Homework", "Project", "Quiz"], help="Choose the type of assignment to categorize it appropriately.")
if assignments_type2 == "Homework":
    st.write("You selected Homework.")
elif assignments_type2 == "Project":
    st.write("You selected Project.")
elif assignments_type2 == "Quiz":
    st.write("You selected Quiz.")

assignments_type3 = st.checkbox("Include Assignment Type", help="Check this box if you want to specify the type of assignment.")
if assignments_type3:
    st.write("Assignment type will be included.")

with st.expander("Additional Options"):
    st.markdown("#### Grading Criteria")
    grading_criteria = st.text_area("Grading Criteria", placeholder="Enter grading criteria for the assignment")
    help="Provide clear grading criteria to help students understand how their work will be evaluated. This can include specific requirements, point distribution, and any other relevant information."

    st.markdown("#### Resources")
    resources = st.text_area("Resources", placeholder="Enter any resources or references for the assignment")
    help="List any resources or references that students can use to complete the assignment. This can include textbooks, websites, articles, or any other materials that may assist them in their work."

with st.expander("Assignment List", expanded=True):
    for a in assignment:
        st.markdown(f"**{a['title']}** - Due: {a['due_date']}")

btn_save = st.button("Save Assignment", use_container_width=True, disabled = True)

import time 
#add new assignments
if btn_save:
    with st.spinner("Saving assignment..."):
        time.sleep(5) # Simulate a delay for saving
        if title == "":
            st.error("Please enter a title for the assignment.")
            st.stop()
            
        new_assignment_id_number = "HW_" + str(next_assignment_id_number)
        next_assignment_id_number += 1
        assignments.append({
            "title": title,
            "due_date": due_date,
            "id": new_assignment_id_number

        })


        st.success("Assignment saved successfully!")
    st.warning("This is a demo. Assignment saving functionality is not implemented yet.")


