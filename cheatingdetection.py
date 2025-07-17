#WE ARE SELLING THIS!!!
import streamlit as st
import requests
URL="https://api.api-ninjas.com/v1/textsimilarity"
API_KEY=st.secrets["api"]["key"]
st.title("Cheating detector.")
st.subheader("Here are the steps to use this program. First, you must sumbit the paper. Than the results will show.")
st.divider()
st.subheader("student 1:")
student1work=st.text_area("Enter Text 1 here")
st.subheader("student 2:")
student2work=st.text_area("Enter Text 2 here")
submit = st.button("Detect Cheating")
st.divider()

if submit:
    headers={ "X-Api-Key":API_KEY}
    body={"text_1":student1work,"text_2":student2work}
    ai_response=requests.post(url=URL,headers=headers, json=body)
    ai_response_result=ai_response.json()
   
    percentage=round(float(ai_response_result["similarity"]) * 100)
    st.info(f"there is a {percentage}% simalarity between student1 and student2")
    if percentage>=90:
       st.write("Cheating")
    elif percentage>=60:
        st.write("maybe cheating")
    else:
        st.write("completely original")














st.divider()
st.subheader("Made by Wyatt Velez/2025")
