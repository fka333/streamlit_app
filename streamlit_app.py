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
fruit_choice = streamlit.text_input('What fruit do you want to have more information about?', 'kiwi')
streamlit.write(f'The user has entered: {fruit_choice}')

fruityvice_response = requests.get(f'https://fruityvice.com/api/fruit/{fruit_choice}')

# Beatify fruityvice advice section
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST;")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write(f'Thanks for adding {add_my_fruit}')

my_cur.execute("insert into fruit_load_list values ('from streamlit')");
