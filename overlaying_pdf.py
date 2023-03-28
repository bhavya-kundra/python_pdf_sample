import PyPDF2
minutesFile = open('python pdf file directory', 'rb') # Enter your pdf file name or directory
pdfReader = PyPDF2.PdfReader(minutesFile)
minutesFirstPage = pdfReader.pages[0]
pdfWatermarkReader = PyPDF2.PdfReader(open('python pdf file directory', 'rb')) # Enter your pdf file name or directory
minutesFirstPage.merge_page(pdfWatermarkReader.pages[0])
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(minutesFirstPage)

for pageNum in range(1, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)

resultPdfFile = open('python pdf file directory', 'wb') # Enter your pdf file name or directory
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()