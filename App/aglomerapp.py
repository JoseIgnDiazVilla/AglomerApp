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
import datetime

called = False

app_state = "Home"

dia =  {0:"Lunes",
		1:"Martes",
		2:"Miercoles",
		3:"Jueves",
		4:"Viernes",
		5:"Sabado",
		6:"Domingo"}

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
    
    main_bg = "background_3.jpg"
    main_bg_ext = "jpg"

    side_bg = "sidebar_3_1.jpg"
    side_bg_ext = "jpg"

    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color:#311A95 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
        
        
    #is_loaded_header.subheader("Bienvenido a AglomerApp")
    
        
    
    st.markdown('<style>h1{color: black;}</style>', unsafe_allow_html=True)
    
    # Fecha
    now = datetime.datetime.now()
    d = datetime.datetime.today().weekday()
    st.sidebar.title("{} {} | {}:{}".format(dia[d], now.day, now.hour, now.minute))
    
    
    # Menu
    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Please select a page", ["Homepage",
                                                             "Iniciar Sesion",
                                                             "Mapa de Densidad",
                                                             "Aglomeracion",
                                                             "Nosotros",
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
    elif app_mode == "Nosotros":
        load_mission()
    elif app_mode == "Contacto":
        load_contact()
    
    numb = np.random.randint(4)
    #st.image("mountain_" + str(numb) + ".jpg",
    #         use_column_width=True)

def load_homepage() -> None:
    #st.markdown('<style>h1{color: white;}</style>', unsafe_allow_html=True)
    #st.title("AglomerAPP")
    st.image("LOGO2.png",
             use_column_width=True)
    st.markdown(
    """
    <h1 style=color:white> Bienvenido a Aglomerapp </h1>
    <ol style=color:white>
    <li>Ingresa a tu portal</li>
    <li>Busca tu destino</li>
    <li>Nosotros te decimos su estado de aglomeración</li>
    <li>Prepara tu mascarilla y alchol gel y comienza tu aventura!</li>
    </ol> 
        
    """, unsafe_allow_html=True)



    
    
    
def load_mission() -> None:
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color:#FFFFFF
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    #st.title("Nuestro Equipo")
    st.markdown(
    """
    <h1 style=color:#311A95> 
    Misión
    </h1>
    <p style=font-size:20px;> 
    <i><b style=text-align: justify;>"Somos un equipo de estudiantes jóvenes, ávidos de nuevos desafíos, decididos a mejorar la calidad de vida de nuestro entorno, con tecnología y entusiasmo" 
    </b></i>
    </p>
    <p>
    El conocimiento y aprendizaje que nos entrega la sociedad debe ser devuelto a través de soluciones tecnológicas que permitan mejorar la calidad de vida de la comunidad.
    </p>
    <h1 style=color:#311A95> 
    Nuestro Equipo
    </h1>
    <p>
    Somos un grupo de cinco estudiantes de ingeniería eléctrica, cuyos conocimientos abarcan desde sistemas de potencia a inteligencia artificial.  
    </p> 
    """,
    unsafe_allow_html=True)
    st.image("fb.png", width=200)
    st.write("Francisco Barrera")
    st.image("ab.png", width=200)
    st.write("Álvaro Becerra")
    st.image("jd.png", width=200)
    st.write("José Díaz")
    st.image("ao.png", width=200)
    st.write("Adolfo Obligado")
    st.image("bp.png", width=200)
    st.write("Bruno Perez")
    
    #numb = np.random.randint(4)
    #st.image("mission_stock_" + str(numb) + ".jpg",
    #         use_column_width=True)
    #st.markdown("Nos comprometemos a")
    #st.write("Evite las aglomera...")
    #st.write("Porque AglomerApp...")
    #t = "<p style='color:white'>This is a paragraph.</p>"
    #st.markdown(t, unsafe_allow_html=True)

 


feedback_backup = pd.DataFrame({"feedback":[]}) 
    
def load_contact() -> None:
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color:#FFFFFF
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <h1 style=color:#311A95> 
    Contacto
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("¿Tienes preguntas o sugerencias? ")
    st.markdown("Escríbenos!")
    
    feed_back = st.text_area("","")
    
    if st.button("Enviar"):
        feedback_backup.append({"feedback":feed_back}, ignore_index=True)
        st.success("Gracias por sus comentarios.")
        
    
    
    st.markdown("Mail: contacto@aglomerapp.cl")
    st.markdown("Telefono: +56 22 786 5806")
    

    
    
if __name__ == "__main__":
    main()
