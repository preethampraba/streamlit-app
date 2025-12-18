import streamlit as st 
import pandas as pd
import plotly.express as px 
uploaded_file=st.file_uploader("Upload your CSV file",type=["csv"])
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data.head())
    columns=list(data.columns)
    target=st.selectbox('choose a target:',columns)
    col2=columns.copy()
    col2.remove(target)
    x_var=st.selectbox('choose an x variable:',col2)
    y_var=st.selectbox('choose an y variable:',col2)
    plot_type=st.selectbox('choose plot type:',['scatter','Line','Bar','pie','histogram'])
    if plot_type =='scatter':
        fig=px.scatter(data,x=x_var,y=y_var,color=target)
    elif plot_type =='Line':
        fig=px.line(data,x=x_var,y=y_var,color=target)
    elif plot_type =='Bar':
        fig=px.Bar(data,x=x_var,y=y_var,color=target)
    elif plot_type =='pie':
        fig=px.pie(data,x=x_var,y=y_var,color=target)
    elif plot_type == 'histogram':
        fig=px.histogram(data,x=x_var,y=y_var,color=target)  
    
    st.plotly_chart(fig)
    
        
