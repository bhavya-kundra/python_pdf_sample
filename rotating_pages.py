import PyPDF2
minutesFile = open('python pdf file directory', 'rb') # Enter your pdf file name or directory
pdfReader = PyPDF2.PdfReader(minutesFile)
page = pdfReader.pages[0]
page.rotate(90)
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)
resultPdfFile = open('python pdf file directory', 'wb') # Enter your pdf file name or directory
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
