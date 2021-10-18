from fastapi import FastAPI,Path
from typing import Optional
from fastapi.param_functions import File
from pydantic import BaseModel
from pdf2jpg import pdf2jpg
import pytesseract
import re

app = FastAPI()

name_of_the_file =''

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None

class UpdateItem(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None
    brand : Optional[str] = None

inventory ={
    1:{
        'name' : 'Milk',
        'price' : 200,
        'brand' : 'Amul'
    },
    2:{
        'name' : 'Chocolate',
        'price' : 20,
        'brand' : 'Dairy Milk'
    }
}

@app.get('/')
def home(): 
    return {'Data' : 'Testing'}

@app.get('/about')
def about():
    return {'Data': 'About'}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description = 'Enter the item id of the item you would like to view', gt = 0)):
    return (inventory[item_id])

@app.get('/get-by-name')
def get_by_name(*,name : Optional[str] = None, test : int):
    for item_id in inventory:
        if(inventory[item_id].name == name):
            return (inventory[item_id])
    return ({'Data' : 'No data found'})

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

@app.post('/create-item/{item_id}')
def create_item(*,item_id : int,item : Item):
    if(item_id in inventory):
        return {"Error" : 'Item id already exists'}
    inventory[item_id] = item
    return(inventory[item_id])

@app.put('/update-item/{item_id}')
def update_item(item_id : int, item : UpdateItem):
    if(item_id not in inventory):
        return({'Error' : 'Item id does not exist'})
    elif(item.name != None):
        inventory[item_id].name = item.name
    elif(item.price != None):
        inventory[item_id].price = item.price
    elif(item.brand != None):
        inventory[item_id].brand = item.brand
    return inventory[item_id]
    