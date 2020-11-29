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

	st.title("Que bueno volver a verte")

	#menu = ["Home","Login","SignUp"]
	#choice = st.sidebar.selectbox("Menu",menu)

	state = 'login'
	st.subheader("Login Section")

	username = st.sidebar.text_input("User Name")
	password = st.sidebar.text_input("Password",type='password')
	if st.sidebar.button("Aceptar"):
		# if password == '12345':
		create_usertable()
		hashed_pswd = make_hashes(password)

		result = login_user(username,check_hashes(password,hashed_pswd))
		if result:

			st.success("Logged In as {}".format(username))

			task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
			if task == "Add Post":
				st.subheader("Add Your Post")

			elif task == "Analytics":
				st.subheader("Analytics")
			elif task == "Profiles" and username == "admin":
				st.subheader("User Profiles")
				user_result = view_all_users()
				clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
				st.dataframe(clean_db)
		else:
			st.warning("Incorrect Username/Password")
	#else:
	#	load_page()
	elif st.sidebar.button("Back"):
		state = 'Home'
		return state





if __name__ == '__main__':
	main()