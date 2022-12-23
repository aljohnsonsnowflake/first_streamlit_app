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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#displays the data pulled from csv file as a table
streamlit.dataframe(my_fruit_list)
