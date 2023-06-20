import streamlit
import pandas as pd

streamlit.title('New Healthy Diner')

streamlit.header('Breakfast')
streamlit.text('Oatmeal')
streamlit.text('Smoothie')
streamlit.text('Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
