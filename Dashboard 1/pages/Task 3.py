import numpy as np 
import pandas as pd 
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
import plotly.express as px

st.set_page_config(page_title='Task 3', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.sidebar.success("Select a task ")

TTF_data = pd.read_excel('price_info.xlsx', sheet_name='TTF')
Brent_data = pd.read_excel('price_info.xlsx', sheet_name='Brent')

#Want to understand Brent_data first 
print('""""""""""""""')
print(Brent_data.head())
print('""""""""""""""')

print('""""""""""""""')
print(Brent_data.tail())
print('""""""""""""""')

print('""""""""""""""')
print(Brent_data.dtypes)
print('""""""""""""""')

print('""""""""""""""')
print(Brent_data.shape)
print('""""""""""""""')

print('""""""""""""""')
#
print(Brent_data.count())
print('""""""""""""""')

#cleaning the Brent_data
Brent_data.dropna(inplace=True)
Brent_data.rename(columns={'%TFM 1!-ICN':'Last','%BRN 1!-ICE': 'Last'}, inplace=True)
print(Brent_data)

#cleaning the TTF_data
TTF_data.dropna(inplace=True)
TTF_data.rename(columns={'%TFM 1!-ICN':'Last','Unnamed: 2':'Volume','Unnamed: 3': 'Last[S:USD/MMBTU]'}, inplace=True)



selected_column = st.selectbox("Select a Column:", ['TTF Price', 'Brent Price','Comparison'])


if selected_column == 'TTF Price':
    plt.title("Movement of TTF price with Time")
    TTF_plot = sns.lineplot(x='Time Series', y='Last[S:USD/MMBTU]', data=TTF_data)
    TTF_plot.set(xlabel='Date', ylabel='Price (in USD/MMBtu)')
    st.plotly_chart(TTF_plot.get_figure())
elif selected_column == 'Brent Price': 
    plt.title("Movement of Brent price with Time")
    Brent_plot = sns.lineplot(x='Time Series', y='Last', data=Brent_data)
    Brent_plot.set(xlabel='Time', ylabel='Price (%Brent)')
    st.plotly_chart(Brent_plot.get_figure())
else:
    TTF_plot = sns.lineplot(x='Time Series', y='Last[S:USD/MMBTU]', data=TTF_data, color='blue', label='Price (in USD/MMBtu)')
    Brent_plot = sns.lineplot(x='Time Series', y='Last', data=Brent_data, color='green', label='Price (%Brent)')
    Brent_plot.set(xlabel='Date', ylabel='Price')
    plt.legend(title='Datasets')
    st.plotly_chart(Brent_plot.get_figure())

    st.markdown("From the comparison, we can see that TTF and Brent prices have a linear relationship. This is supported when we see that TTF prices increases when Brent prices increases. ")
