import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞 Sandwiches')
streamlit.text('🥣 Poha')
streamlit.text('🥣 Upma')
streamlit.text('🥗 Masala Dosa')
streamlit.text('🐔 Omelette')
streamlit.text('🥑 Vanila Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
