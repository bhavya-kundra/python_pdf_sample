import PyPDF2
pdfReader = PyPDF2.PdfReader(open(r"python pdf file directory", 'rb')) # Enter your pdf file name or directory
pdfReader.is_encrypted
pdfReader.pages[0]

pdfReader = PyPDF2.PdfReader(open(r"python pdf file directory", 'rb')) # Enter your pdf file name or directory
pdfReader.decrypt('rosebud')
pageObj = pdfReader.pages[0]
print(pageObj)