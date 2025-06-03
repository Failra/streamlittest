import streamlit as st

st.title("Dog Age Calculator")

dogName = st.text_input("Enter your dog's name: ")

dogAge = st.number_input("Enter your dog's age: ")

if st.button("Calculate Dog Year's"):
    if dogName and dogAge:
        dogYears = dogAge * 7
        st.write(dogName, "is", dogYears, "dog years old")

