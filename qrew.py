import streamlit as st

col1,col2 = st.colums([2,3])

with col1 :
    st.title('here is column1')
with col2 :
    st.title('here is column2')
    st.checkbox('this is checkbox1 in col2')

col1.subheader(' i am column1 subheaer ! ! ')
col2.checkbos('this is checkbox2 in col2')