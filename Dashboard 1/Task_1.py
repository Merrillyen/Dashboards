import numpy as np 
import pandas as pd 
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as px

st.set_page_config(page_title='Task 1', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.write("Yen Wei Yang Merrill Dashboard👋")

st.sidebar.success("Select a task ")

TTF_data = pd.read_excel('price_info.xlsx', sheet_name='TTF')
JKM_data = pd.read_excel('price_info.xlsx', sheet_name='JKM')
Brent_data = pd.read_excel('price_info.xlsx', sheet_name='Brent')

#Want to understand TTF_data first 
print('""""""""""""""')
print(TTF_data.head())
print('""""""""""""""')

print('""""""""""""""')
print(TTF_data.tail())
print('""""""""""""""')

print('""""""""""""""')
print(TTF_data.dtypes)
print('""""""""""""""')

print('""""""""""""""')
print(TTF_data.shape)
print('""""""""""""""')

print('""""""""""""""')
#
print(TTF_data.count())
print('""""""""""""""')

#cleaning the data
TTF_data.dropna(inplace=True)
TTF_data.rename(columns={'%TFM 1!-ICN':'Last','Unnamed: 2':'Volume','Unnamed: 3': 'Last[S:USD/MMBTU]'}, inplace=True)

plt.figure(figsize=(14,6))

plt.title("Hourly movement of trading volume for TTF")

plot_volume = sns.lineplot(x='Time Series', y='Volume', data=TTF_data)
plot_volume.set(xlabel='Date', ylabel='Volume')

plt.figure(figsize=(14,6))

plt.title("Hourly movement of price for TTF")

plot_price = sns.lineplot(x='Time Series', y='Last[S:USD/MMBTU]', data=TTF_data)
plot_price.set(xlabel='Date', ylabel='Price (in USD/MMBtu)')

st.plotly_chart(plot_volume.get_figure())
st.plotly_chart(plot_price.get_figure())