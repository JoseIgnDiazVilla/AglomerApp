import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import pydeck as pdk

import streamlit as st
import pandas as pd


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

def load_page():
    
	st.title("Aglomeracion de tu destino")
	
    
	place = st.selectbox("Destino", list(places_data.keys()))


	n_people = np.random.randint(300)
	index = n_people/places_sizes[place]
	st.markdown("La aglomeracion en {} tiene un indice de {}.".format(place, index))
    
	if index < 0.3:
		st.image("green.jpg")
		st.markdown("{} no esta aglomerado! No hay problema en ir.".format(place))
	elif index < 0.7:
		st.image("yellow.jpg")
		st.markdown("{} Tiene mediana aglomeracion. Tome precauciones.".format(place))
	else:
		st.image("red.jpg")
		st.markdown("{} Tiene demasiada aglomeracion. Prefiera alternativas.".format(place))
        
	st.write("Vas a ir?")
	st.button("Si")
    
	st.slider("Aglomeracion")
        
	latitud, longitud = places_data[place]  
	map_data = pd.DataFrame(
		0*np.random.randn(1, 2) / [50, 50] + [latitud, longitud],
		columns=['lat', 'lon'])

	st.map(map_data, zoom=17)
        
        


