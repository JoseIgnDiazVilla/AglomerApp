#from vega_datasets import data
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import time
import login
import signup
import base64
import login_signup
import mapa
import aglomeracion

called = False

app_state = "Home"

def main():
    #page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    create_layout()
    #if page == "Homepage":
    #    st.header("This is your data explorer.")
    #    st.write("Please select a page on the left.")
    #    st.write(df)
    #elif page == "Exploration":
    #    st.title("Data Exploration")
    #    x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
    #    y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
    #    visualize_data(df, x_axis, y_axis)

@st.cache
def load_data():
    df = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40]
    })
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)
    

def create_layout() -> None:
    """ Create the layout after the data has succesfully loaded

    
    """
    global app_state
    
    main_bg = "back_ground2 (2).jpg"
    main_bg_ext = "jpg"

    side_bg = "sidebar.jpg"
    side_bg_ext = "jpg"

    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url(data:images/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
        }}
       .sidebar .sidebar-content {{
            background: url(data:images/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
        
        
    #is_loaded_header.subheader("Bienvenido a AglomerApp")
    
        
    
    st.markdown('<style>h1{color: black;}</style>', unsafe_allow_html=True)
    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Please select a page", ["Homepage",
                                                             "Iniciar Sesion",
                                                             "Mapa de Densidad",
                                                             "Aglomeracion",
                                                             "Mision",
                                                             "Contacto"])
    if app_mode == 'Homepage':
        load_homepage()
    if app_mode == "Iniciar Sesion":
        login_signup.load_page()
    elif app_mode == "Mapa de Densidad":
        mapa.load_page()
    elif app_mode == "Aglomeracion":
        aglomeracion.load_page()
    elif app_mode == "Player Statistics":
        playerstats.load_page(df, player_list)
    elif app_mode == "Mision":
        exploregames.load_page(df, player_list)
    elif app_mode == "Contacto":
        headtohead.load_page(df, player_list)
    
    numb = np.random.randint(4)
    st.image("mountain_" + str(numb) + ".jpg",
             use_column_width=True)

def load_homepage() -> None:
    #st.markdown('<style>h1{color: white;}</style>', unsafe_allow_html=True)
    #st.title("AglomerAPP")
    st.image("logo.png",
             use_column_width=True)
    st.markdown("XX__Bienvenide__XX")
    
    st.write("Evite las aglomera...")
    
    st.write("Porque AglomerApp...")
    
    
    t = "<div>Hello there my <span class='highlight white'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"

    
    
    
def reset_buttons():
    
    login = False
    signup = False
    app_mode = "Portada"
    
    
if __name__ == "__main__":
    main()