from pdf2jpg import pdf2jpg
inputpath = r"C:\Users\sanje\Desktop\Week1\example1.pdf"
outputpath = r"C:\Users\sanje\Desktop\Week1"


result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
print(result)

 