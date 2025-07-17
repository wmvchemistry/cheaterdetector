#WE ARE SELLING THIS!!!
import streamlit as st
import requests
from io import StringIO  # text files
import PyPDF2  #F pdfs
from docx import Document  # docx, sheets

# Helper function to extract text
def extract_text_from_file(file):
    try:
        if file.name.endswith(".txt"):
            return StringIO(file.getvalue().decode("utf-8")).read()
        elif file.name.endswith(".docx"):
            doc = Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        elif file.name.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        else:
            st.warning("Unsupported file type. Please upload .txt, .docx, or .pdf")
            return ""
    except Exception as e:
        st.error(f"Error reading file {file.name}: {e}")
        return ""
URL="https://api.api-ninjas.com/v1/textsimilarity"
API_KEY=st.secrets["api"]["key"]
st.title("Cheating detector.")
st.subheader("Here are the steps to use this program. First, you must sumbit the paper. Than the results will show.")
st.divider()
st.subheader("student 1:")
student1work=st.text_area("Enter Text 1 here")
student1file=st.file_uploader("upload the work",key="file1")
st.subheader("student 2:")
student2work=st.text_area("Enter Text 2 here")
student2file=st.file_uploader("upload the work",key="file2")
submit = st.button("Detect Cheating")
st.divider()

if submit:
    if student1file:
        student1work=extract_text_from_file(student1file)
    if student1file:
        student1work=extract_text_from_file(student2file)
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
