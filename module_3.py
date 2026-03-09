import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")
st.title("Course Manager App")

# --- DATA LOADING ---
json_file = Path("users.json")
users = []
if json_file.exists():
    with open(json_file, "r") as f:
        users = json.load(f)


# --- LOGIN ---
st.subheader("Log In")
with st.container(border=True):
    email_input = st.text_input("Email", key="login_email")
    password_input = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Log In"):
        with st.spinner("Logging in..."):
            time.sleep(2) # Fake backend delay
            
            # Find user
            found_user = None
            for user in users:
                if user["email"].strip().lower() == email_input.strip().lower() and user["password"] == password_input:
                    found_user = user
                    break
            
            if found_user:
                st.success(f"Welcome back, {found_user['email']}!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Invalid credentials")

# --- REGISTRATION ---
st.subheader("New Instructor Account")
with st.container(border=True):
    new_email = st.text_input("Email Address", key="reg_email")
    new_password = st.text_input("Password", type="password", key="reg_password")
    
    if st.button("Create Account"):
        with st.spinner("Creating account..."):
            time.sleep(2) # Fake backend delay
            # ... (Assume validation logic here) ...
            users.append({
                "id": str(uuid.uuid4()),
                "email": new_email,
                "password": new_password,
                "role": "Instructor"
            })
            with open(json_file, "w") as f:
                json.dump(users, f, indent=4)
            st.success("Account created!")
            st.rerun()

st.write("---")
st.dataframe(users)

email_input = st.text_input("Email", key="login_email")
password_input = st.text_input("Password", type="password", key="login_password")

new_email = st.text_input("Email Address", key="reg_email")
new_password = st.text_input("Password", type="password", key="reg_password")

# Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None

if "role" not in st.session_state:
    st.session_state["role"] = None 

if "page" not in st.session_state:
    st.session_state["page"] = "login" # or 'register'

if st.button("Log In", type="primary"):
        with st.spinner("Logging in..."):
            time.sleep(2)
            
            # ... (search for user logic) ...
            
            if found_user:
                # 1. SAVE the user to session state (The App remembers!)
                st.session_state["logged_in"] = True
                st.session_state["user"] = found_user
                st.session_state["role"] = found_user["role"] # The Role is Critical!
                
                st.success("Login Successful!")
                time.sleep(1)
                st.rerun()  # Force a redraw immediately
            else:
                st.error("Invalid credentials")
if st.session_state["role"] == "Admin":
    st.header("Admin Dashboard")
    st.success(f"Hello, {st.session_state['user']['full_name']} ({st.session_state['role']})")
    
    # Logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.session_state["role"] = None
        st.rerun()

elif st.session_state["role"] == "Instructor":
    st.header("Instructor Dashboard")
    st.success(f"Welcome, {st.session_state['user']['full_name']}!")
    
    # Logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.session_state["role"] = None
        st.rerun()

else:
    # GUEST VIEW (Login or Register)
    if st.session_state["page"] == "login":
        # ... Show Login Form ...
        pass
    else:
        # ... Show Register Form ...
        pass








