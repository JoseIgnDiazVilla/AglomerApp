import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import pydeck as pdk

import streamlit as st
import pandas as pd


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data



def load_page():
    """Simple Login App"""
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color:#FFFFFF
        }}
        </style>
        """,
        unsafe_allow_html=True)
    for i in range(5):
        st.write('')
    
    st.markdown(
    """
    <h1 style=color:#311A95> Ingresa Aquí
    """, unsafe_allow_html=True)

    #menu = ["Login","SignUp"]
    #choice = st.sidebar.selectbox("Menu",menu)
    
    st.sidebar.title("Inicio")
    
    choice = st.sidebar.selectbox("Inicio", ["Login",
                                            "SignUp"])
    
    
    st.sidebar.write("")
    st.sidebar.write("No tienes cuenta?")

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Ingresa Aquí")

        username = st.text_input("Usurario")
        password = st.text_input("Contraseña",type='password')
        if st.button("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                if username == "admin":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")





    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")



if __name__ == '__main__':
    main()
    
map_data = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [-33.4579315, -70.663987],
    columns=['lat', 'lon'])
        


