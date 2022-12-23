import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
#using pandas to read csv file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#to get the names of the fruit rather than its associated number
my_fruit_list = my_fruit_list.set_index('Fruit')

#Lets users pick fruits they want to includ
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#Pre-populate the user's selection with Avocado and Strawberries & save it in the variable fruits_selected
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

#pulls the rows in our csv file based on the fruits_selected & save it in the variable fruits_to_show
fruits_to_show = my_fruit_list.loc[fruits_selected]
#displays the data pulled from csv file as a table
streamlit.dataframe(fruits_to_show)
