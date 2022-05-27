import streamlit

streamlit.title('Hello World!')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

data = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# create item picker
# make pre-selection with Avocado and Strawberries
selections = streamlit.multiselect('Pick some fruits: ', list(data.index), ['Avocado', 'Strawberries'])
fruit_to_show = data.loc[selections]
streamlit.text(selections)

# display dataframe of fruit macro
streamlit.dataframe(fruit_to_show)
