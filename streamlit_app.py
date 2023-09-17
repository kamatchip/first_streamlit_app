import streamlit
import pandas
streamlit.title('My Parents Healthy Diner')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#pick some fruits
streamlit.multiselect("Pick some fruits :",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
