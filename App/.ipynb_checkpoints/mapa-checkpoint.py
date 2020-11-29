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

places_data = {"FCFM":[-33.457821206971616, -70.66270978455834],
				"Cerro Calan": [-33.39702942966838, -70.53744836281406],
				"Estadio Nacional": [-33.46494589502118, -70.61063201399021],
				"GAM": [-33.439290696460965, -70.63979835524397],
				"Facultad de Medicina": [-33.418973836650125, -70.65332597428556]}

def load_page():
    
	st.title("Mapa")
	#st.write(list(places_data.keys()))
	latitud, longitud = [-33.457821206971616, -70.66270978455834]
	if st.checkbox("Custom"):
		latitud = st.number_input("Latitud")
		longitud = st.number_input("Longitud")
        
	else: 
		print(places_data.keys())
		place = st.selectbox("Destino", list(places_data.keys()))
		latitud, longitud = places_data[place]
        
	map_data = pd.DataFrame(
		np.random.randn(200, 2) / [50, 50] + [latitud, longitud],
		columns=['lat', 'lon'])

	st.map(map_data, zoom=17)
        
        


