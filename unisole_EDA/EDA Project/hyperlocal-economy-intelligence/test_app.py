import streamlit as st
import pandas as pd
#st.title("My first app")
#st.write("hello everyone")

## some basic elements
st.title("Main Title")
st.header("section hearder")
st.subheader("sub section")
st.text("palin text")
st.write("most flexible: work with text, data table, charts")

### 
df=pd.read_csv('hyperlocal_economy_processed.csv')

st.dataframe(df)

## select box
city=st.selectbox("select your city",df['city'].unique())

## side bar 
age= st.slider("select age",18,60)

## button
if st.button("click me"):
    st.write("button clicked")


## side bar
st.sidebar.title("filters")
city=st.sidebar.selectbox("cities",df["city"])

## charts in streamlit
st.line_chart(df["monthly_rent"])