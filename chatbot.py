import streamlit as st  # type: ignore

#uploading the pdf files 

st.header("my first chatbot")

with st.sidebar:
    st.title("your title")
    file=st.file_uploader("upload pdf file",type="pdf")