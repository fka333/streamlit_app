import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Hello World!')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

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

def get_fruityvice_data(this_fruit):
  fruityvice_response = requests.get(f'https://fruityvice.com/api/fruit/{this_fruit}')
  # Beatify fruityvice advice section
  return pd.json_normalize(fruityvice_response.json())


# New section
streamlit.header('Fruityvice Fruit Advices!')

try:
  fruit_choice = streamlit.text_input('What fruit do you want to have more information about?', 'kiwi')
  if not fruit_choice:
    streamlit.error('Please select one fruit to get information!')
  else:
    streamlit.write(f'The user has entered: {fruit_choice}')
    back_from_function = get_fruityvice_data(fruit_choice)
    # output as a table
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
 
# Fruit load list
streamlit.header('View Our Fruit List - Add Your Favorite')

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST;")
    return my_cur.fetchall()

# Add a button
if streamlit.button('Get fruit list!'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
 

# Allow end user to insert more fruit
def insert_row_sf(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "');")
    return f'Thanks for adding {new_fruit}'

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add more fruit!'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_sf(add_my_fruit)
  streamlit.text(back_from_function)
  
# stop
streamlit.stop()  

