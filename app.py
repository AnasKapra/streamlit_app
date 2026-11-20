import streamlit as st 
import os
st.title("This is the form")
st.header("Fill your form")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age",min_value=18,max_value=100,step=5)
gender=st.selectbox("Select your gender",["male","female"])
subject=st.multiselect("Select your choice",["python","sql","ml","cs"])
submit=st.button("Submit")
st.image(os.path.join(os.getcwd(),"static","23.jpg"))
if submit:
    st.success("Form submitted sucessfully")
    st.write(f"your name is {name}")
    st.write(f"your age is {age}")
    st.write(f"your gender is {gender}")
    st.write(f"your subject is {subject}")
    st.divider()
    st.image(r"E:\hd_pics")