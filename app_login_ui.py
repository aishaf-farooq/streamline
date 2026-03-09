import streamlit as st
import json
import os
import time
import json
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Course Manager", layout="centered")

st.title("Course Manager")

json_file = Path( "users.json")

# load users
if json_file.exists():
    with open(json_file, "r") as file:
        users = json.load(file)
else:
    users = [
    {
        "id": "1",
        "email": "admin@school.edu",
        "full_name": "System Admin",
        "password": "123ssag@43AE",
        "role": "Admin"
    }
]

page = st.sidebar.radio("Choose an option", ["Register", "Login"])

# REGISTER PAGE
if page == "Register":
    st.header("New Instructor Account")

    email = st.text_input("Email Address")
    full_name = st.text_input("First and Last Name")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Instructor"])

    create_btn = st.button("Create Account")

    if create_btn:
        with st.spinner("Creating your account..."):
            time.sleep(1)

            new_user = {
                "id": str(len(users) + 1),
                "email": email,
                "full_name": full_name,
                "password": password,
                "role": role,
                "registered_at": str(datetime.now())
            }

            users.append(new_user)

            with open(json_file, "w") as file:
                json.dump(users, file, indent=4)

        st.success("Account created successfully!")

# LOGIN PAGE
if page == "Login":
    st.header("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    login_btn = st.button("Log In")

    if login_btn:
        found_user = False

        with st.spinner("Verifying credentials..."):
            time.sleep(1)

            for user in users:
                if user["email"] == email and user["password"] == password:
                    found_user = True
                    st.success("Welcome back " + user["full_name"] + "!")
                    st.write("Role:", user["role"])
                    st.write("Registered at:", user["registered_at"])

            if found_user == False:
                st.error("Invalid email or password.")

    st.subheader("Current Users")
    st.dataframe(users)