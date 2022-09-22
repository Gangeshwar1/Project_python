# importing required modules
import PyPDF2
	
# creating a pdf file object
pdfFileObj = open('Program/TATA.pdf', 'rb')
	
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
# printing number of pages in pdf file
print(pdfReader.numPages)
	
# creating a page object
pageObj = pdfReader.getPage(0)
	
# extracting text from page
print(pageObj.extractText())

from PyPDF2 import PdfReader

reader = PdfReader("Program/TN_24.08.2020.pdf")
text = reader.pages[0].extract_text()
assert "Directorate" in text, text
	
# closing the pdf file object
pdfFileObj.close()
