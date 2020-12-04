import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import pydeck as pdk

import streamlit as st
import pandas as pd

import datetime

dia =  {0:"Lunes",
		1:"Martes",
		2:"Miercoles",
		3:"Jueves",
		4:"Viernes",
		5:"Sabado",
		6:"Domingo"}

places_data = {"FCFM":[-33.457821206971616, -70.66270978455834],
				"Cerro Calan": [-33.39702942966838, -70.53744836281406],
				"Estadio Nacional": [-33.46494589502118, -70.61063201399021],
				"GAM": [-33.439290696460965, -70.63979835524397],
				"Facultad de Medicina": [-33.418973836650125, -70.65332597428556]}

places_sizes = {"FCFM":200,
				"Cerro Calan": 100,
				"Estadio Nacional": 1000,
				"GAM": 200,
				"Facultad de Medicina": 400}

places_trends = {"FCFM": np.random.randint(200, size=7*24),
				"Cerro Calan": np.random.randint(100, size=7*24),
				"Estadio Nacional": np.random.randint(1000, size=7*24),
				"GAM": np.random.randint(200, size=7*24),
				"Facultad de Medicina": np.random.randint(400, size=7*24)}

def load_page():
	st.markdown('<style type="text/css"> p {color:white;} </style>', unsafe_allow_html=True)
	st.title("Aglomeracion de tu destino")
	now = datetime.datetime.now()
	d = datetime.datetime.today().weekday()
	#st.markdown("{} {} | {}:{}".format(dia[d], now.day, now.hour, now.minute))
    
	place = st.selectbox("Destino", list(places_data.keys()))


	n_people = places_trends[place][d*now.hour]
	index = n_people/places_sizes[place]
	tex = st.empty()
	tex.markdown("La aglomeracion en {} tiene un indice de {}.".format(place, index))
    
	prog = st.empty()
	prog.progress(min(index, 1.0))
    
	if index < 0.3:
		st.image("green.jpg")
		st.success("{} no esta aglomerado! No hay problema en ir.".format(place))
		#st.balloons()
	elif index < 0.7:
		st.image("yellow.jpg")
		st.success("{} Tiene mediana aglomeracion. Tome precauciones.".format(place))
	else:
		st.image("red.jpg")
		st.warning("{} Tiene demasiada aglomeracion. Prefiera alternativas.".format(place))
        
	#st.write("Vas a ir?")
	if st.button("Vas a este lugar?"):
		places_trends[place][d*now.hour] += 1
        
		n_people = places_trends[place][d*now.hour]
		index = n_people/places_sizes[place]
        
		tex.markdown("La aglomeracion en {} tiene un indice de {}.".format(place, index))
        
		prog.progress(min(index, 1.0))
		st.write("Entendido, tenga un buen viaje")
        
	latitud, longitud = places_data[place]  
	map_data = pd.DataFrame(
		0*np.random.randn(1, 2) / [50, 50] + [latitud, longitud],
		columns=['lat', 'lon'])

	st.map(map_data, zoom=17)
        
        


