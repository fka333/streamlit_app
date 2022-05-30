import streamlit

streamlit.title('Hello World!')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

# extract data 
data = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
data = data.set_index('Fruit')

# create item picker
# make pre-selection with Avocado and Strawberries
selections = streamlit.multiselect('Pick some fruits: ', list(data.index), ['Avocado', 'Strawberries'])
fruit_to_show = data.loc[~data.index.isin(selections)]
streamlit.text(selections)

# display dataframe of fruit macro
streamlit.dataframe(fruit_to_show)

# New section
streamlit.header('Fruityvice Fruit Advices!')

import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/banana')

# Beatify fruityvice advice section
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output as a table
streamlit.dataframe(fruityvice_normalized)




