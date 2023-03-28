import PyPDF2

pdfFileObj = open(r"python pdf file directory", 'rb') # Enter your pdf file name or directory

pdfReader = PyPDF2.PdfReader(pdfFileObj)

print(len(pdfReader.pages))

pageObj = pdfReader.pages[0]

print(pageObj)

print(pageObj.extract_text())

pdfFileObj.close()
