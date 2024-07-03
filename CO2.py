# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:21:07 2024

@author: Harshda Yewale
"""

import streamlit as st
import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA
import numpy as np 
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt

air_quality = pd.read_excel("CO2_dataset.xlsx")
air_quality1 = pd.read_excel("CO2_dataset.xlsx",header=0, index_col=0,parse_dates=True )


final_arima = ARIMA(air_quality1['CO2'],order = (5,0,7))
final_arima = final_arima.fit()

st.title("Forecasting CO2 Emission")
nav = st.sidebar.radio("Navigation",["About data","Prediction","Forecast"])
if nav == "About data":
    st.subheader("Data")
    air_quality
    st.subheader("Scatter plot of the data")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(figsize = (10,5))
    plt.scatter(air_quality["CO2"],air_quality["Year"])
    plt.ylim(0)
    plt.xlabel("Years")
    plt.ylabel("CO2 Emission")
    plt.tight_layout()
    st.pyplot()


    st.subheader("Line plot of the data") 
    st.line_chart(data=air_quality.CO2, width=150, height=300, use_container_width=True)
   

    st.subheader("Histogram of the data") 
    fig= plt.figure(figsize=(10,4))
    plt.hist(air_quality.CO2)
    st.pyplot(fig)
 

  
  
if nav == "Prediction":
   predict = final_arima.fittedvalues
   air_quality1["Predicted_CO2"] = predict
   air_quality1
   plt.plot(air_quality1.CO2, label='original',color='black')
   plt.plot(predict, label='Predicted',color='red')
   plt.title('Prediction')
   plt.legend(loc='upper left', fontsize=8)
   st.pyplot()
  


if nav == "Forecast":
    
    year = st.slider("Select number of Year from 2015",1,21,step = 1)

    st.subheader("Forecasting the data for next few years")
    
    
    pred = final_arima.forecast(year)

   
    if st.button("Predict"):
       st.subheader(f"Your predicted CO2 emission from year 2015" )
       pred

       st.subheader("Line plot of the Forecasted data")
       st.line_chart(pred)
       

       st.subheader("Histogram of the Forecasted data") 
       fig1= plt.figure(figsize=(10,4))
       plt.hist(pred)
       st.pyplot(fig1)