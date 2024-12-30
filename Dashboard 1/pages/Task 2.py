import numpy as np 
import pandas as pd 
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as px

st.set_page_config(page_title='Task 2', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.sidebar.success("Select a task ")

TTF_data = pd.read_excel('price_info.xlsx', sheet_name='TTF')
JKM_data = pd.read_excel('price_info.xlsx', sheet_name='JKM')
Brent_data = pd.read_excel('price_info.xlsx', sheet_name='Brent')

#Want to understand JKM_data first 
print('""""""""""""""')
print(JKM_data.head())
print('""""""""""""""')

print('""""""""""""""')
print(JKM_data.tail())
print('""""""""""""""')

print('""""""""""""""')
print(JKM_data.dtypes)
print('""""""""""""""')

print('""""""""""""""')
print(JKM_data.shape)
print('""""""""""""""')

print('""""""""""""""')
#
print(JKM_data.count())
print('""""""""""""""')

plt.figure(figsize=(14,6))

plt.title("Daily movement of LNG price")

plot_price = sns.lineplot(x='Date', y='JKM assessment price', data=JKM_data)
st.plotly_chart(plot_price.get_figure())

st.markdown("The price difference is due higher demand of LNG from Asian countries. A potential strategy would be to buy LNG from closer countries and we can sell it countries that are further.")