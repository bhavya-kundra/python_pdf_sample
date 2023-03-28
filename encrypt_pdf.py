import PyPDF2
pdfFile = open('python pdf file directory', 'rb') # Enter your pdf file name or directory
pdfReader = PyPDF2.PdfReader(pdfFile)
pdfWriter = PyPDF2.PdfWriter()
for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.pages[pageNum])

pdfWriter.encrypt('swordfish')
resultPdf = open('python pdf file directory', 'wb') # Enter your pdf file name or directory
pdfWriter.write(resultPdf)
resultPdf.close()