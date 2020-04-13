import PyPDF2
import sys
import os

template = sys.argv[1]
watermark = sys.argv[2]

template1 = PyPDF2.PdfFileReader(open(template, 'rb')) #creates a file reader
watermark1 = PyPDF2.PdfFileReader(open(watermark, 'rb'))
output = PyPDF2.PdfFileWriter() #creates a write object

for i in range(template1.getNumPages()):#getNumPages gives how many pages the template file has
	page = template1.getPage(i) #take one page at a time
	page.mergePage(watermark1.getPage(0)) #watermark file has only one page
	output.addPage(page)

	with open('watermarked_output2.pdf', 'wb') as file:
		output.write(file)


