import streamlit as st
import requests
import pandas as pd
from pdf2jpg import pdf2jpg
import pytesseract
import re

st.title("Welcome To Invoice Teller!")

st.text("")
st.text("")
st.text("")

s=0
filename = st.text_input('Enter a file path of the invoice pdf :')
name = filename.split('\\')
name = name[len(name)-1]

print(filename)

if (filename is not ""):
    try:
        with open(filename) as input:
            st.success("Successfully "+name+" uploaded")
            s=1
    except FileNotFoundError:
            st.error('File not found.')
    
    
name_of_the_file = name+'_dir\\0_'+name+'.jpg'

inputpath = filename
outputpath = r"C:\Users\sanje\Desktop\Week1"

if(s != 0):
    result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
    print(result)
    try:
        from PIL import Image
    except ImportError:
        import Image

    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sanje\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    # Simple image to string
    all_str = pytesseract.image_to_string(Image.open(name_of_the_file))

    print("number of lines : ",len(all_str))
    print(all_str)

    all_str = all_str.replace(',','')

    temp = re.findall(r"[-+]?\d*\.\d+|\d+", all_str)
    print (temp)

    result =[]

    for i in temp:
        if('.' in i):
            result.append(float(i))


    result = sorted(result)

    result = result[len(result)-1]
    result = 'Total bill amount = '+str(result)

    st.text(result)

# uploaded_file = st.file_uploader("Upload Files",type=['jpg','jpeg','pdf'])
# if uploaded_file is not None:
#     uploaded_file.type = uploaded_file.type.split('/')[1]
#     file = open(uploaded_file.name,'rb')
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    # if st.checkbox("Show/Hide"):
    #     st.write(file_details)
#     st.success("Successfully "+file_details['FileName']+" uploaded")
#     uploaded_file
    
