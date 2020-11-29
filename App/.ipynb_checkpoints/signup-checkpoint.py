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

	st.title("Un gusto conocerte")

	state = "Sign Up"
    
	st.subheader("Create New Account")
	new_user = st.text_input("Username")
	new_password = st.text_input("Password",type='password')

	if st.button("Signup"):
		create_usertable()
		add_userdata(new_user,make_hashes(new_password))
		st.success("You have successfully created a valid Account")
		st.info("Go to Login Menu to login")

	#if st.button("Back"):
	#	return "Home"
        
        


