from fastapi import FastAPI,Path
from typing import Optional
from fastapi.param_functions import File
from pydantic import BaseModel
from pdf2jpg import pdf2jpg
import pytesseract
import re

app = FastAPI()

name_of_the_file =''

@app.get('/')
def home(): 
    return {'Data' : 'Welcome To Home Page'}


@app.get('/convert-pdf-2-image/{file}')
def convert(file : str):
    inputpath = file
    outputpath = r"C:\Users\sanje\Desktop\Week1"

    temp = inputpath.split('\\')
    temp = temp[len(temp)-1]

    name_of_the_file = temp+'_dir\\0_'+temp+'.jpg'


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

    temp = re.findall(r"[-+]?\d*\.\d+|\d+", all_str)
    print (temp)

    result =[]

    for i in temp:
        if('.' in i):
            result.append(float(i))

    print(result)

    result = sorted(result)

    print(result)

    print('Total bill amount is : ',result[len(result)-1])

    return({"Data" : [name_of_the_file,result[len(result)-1]]})
