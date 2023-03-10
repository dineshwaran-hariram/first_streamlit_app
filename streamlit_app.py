import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🐔 Chicken Sandwich 🐔')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie 🥗')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal 🥣')
streamlit.text('\N{egg} Hard-Boiled Free-Range Egg \N{egg}')
streamlit.text('\N{hamburger} Beef Sandwich \N{hamburger}')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalised = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalised)

streamlit.header('FRUITYVICE FRUIT ADVICE!')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()

streamlit.header("Fruit load list:")
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ',add_my_fruit)
fruityvice_response2 = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)

fruityvice_normalised2 = pandas.json_normalize(fruityvice_response2.json())

streamlit.dataframe(fruityvice_normalised2)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
