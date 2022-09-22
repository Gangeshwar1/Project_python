from pdf2docx import Converter
pdf_file = 'Program/TATA.pdf'
docx_file = 'Program/TATA.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
