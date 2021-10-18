try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sanje\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# Simple image to string
all_str = pytesseract.image_to_string(Image.open(r'example.pdf_dir\\0_example.pdf.jpg'))

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