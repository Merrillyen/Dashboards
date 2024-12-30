import numpy as np 
import pandas as pd 
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

st.set_page_config(page_title='Task 4', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.sidebar.success("Select a task ")

TTF_data = pd.read_excel('price_info.xlsx', sheet_name='TTF')
JKM_data = pd.read_excel('price_info.xlsx', sheet_name='JKM')
Brent_data = pd.read_excel('price_info.xlsx', sheet_name='Brent')

#cleaning the data
TTF_data.dropna(inplace=True)
TTF_data.rename(columns={'%TFM 1!-ICN':'Last','Unnamed: 2':'Volume','Unnamed: 3': 'Last[S:USD/MMBTU]'}, inplace=True)

#cleaning the Brent_data
Brent_data.dropna(inplace=True)
Brent_data.rename(columns={'%TFM 1!-ICN':'Last','%BRN 1!-ICE': 'Last'}, inplace=True)

TTF = TTF_data.groupby(TTF_data['Time Series'].dt.to_period('Q'))['Last[S:USD/MMBTU]'].mean()
TTF.set_axis(['2024Q1','2024Q2'])
#JKM = JKM_data.groupby(JKM_data['Time Series'].dt.to_period('Q'))['JKM assessment price'].mean()
Brent = Brent_data.groupby(Brent_data['Time Series'].dt.to_period('Q'))['Last'].mean()
Brent.set_axis(['2024Q1','2024Q2'])
print(TTF)
print(Brent)

plt.figure(figsize=(14,6))
TTF_bar = sns.barplot(TTF)
TTF_bar.set(xlabel='Quarter', ylabel='Price (in USD/MMBtu)')
st.pyplot(TTF_bar.get_figure())

#JKM_bar = sns.barplot(JKM)
#st.plotly_chart(JKM_bar.get_figure())
plt.figure(figsize=(14,6))
Brent_bar = Brent.plot(kind='bar')
Brent_bar.set(xlabel='Quarter', ylabel='Price(%Brent)')
st.pyplot(Brent_bar.get_figure())

st.markdown("Doing a quarter to quarter analysis, we can see that the prices increases from Q1 to Q2.")