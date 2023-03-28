import PyPDF2
pdf1File = open(r"python pdf file directory", 'rb') # Enter your pdf file name or directory
pdf2File = open(r"python pdf file directory", 'rb') # Enter your pdf file name or directory
pdf1Reader = PyPDF2.PdfReader(pdf1File)
pdf2Reader = PyPDF2.PdfReader(pdf2File)
pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdf1Reader.pages)):
    pageObj = pdf1Reader.pages[pageNum]
    pdfWriter.add_page(pageObj)

for pageNum in range(len(pdf2Reader.pages)):
    pageObj = pdf2Reader.pages[pageNum]
    pdfWriter.add_page(pageObj)

pdfOutputFile = open('python pdf file directory', 'wb') # Enter your pdf file name or directory
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
