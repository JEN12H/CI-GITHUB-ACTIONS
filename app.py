import streamlit as st   

st.title("SIMPLE STREAMLIT CALCULATOR")
st.write("ENTER YOUR NUMBER TO CALCULATE ITS SQUARE AND CUBE ")

n = st.number_input("Enter a number:", value=1,step = 1 )

square = n ** 2
cube = n ** 3   
fifth_power = n ** 5

st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth power of {n} is {fifth_power}")