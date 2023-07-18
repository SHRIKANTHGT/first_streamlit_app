import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.title('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Otameal')
streamlit.text('Kale, Spinach & Rocket Smoothe')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.text('🥣 Omega 3 & Blueberry Otameal')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
fruits selected-streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[Avacodo,'straberries'])

