import PyPDF2

with open('dummy.pdf', 'rb') as file: #read binary and renames dummy as file
	reader = PyPDF2.PdfFileReader(file) #renames file as reader
	page = reader.getPage(0) #picks first page of file
	page.rotateCounterClockwise(90) #rotates page
	writer = PyPDF2.PdfFileWriter() #creates a file named writer
	writer.addPage(page) #adds a page to writer
	with open('tilt.pdf', 'wb') as new_file: #wb=write binary, creates a new file tilted.pdf
		writer.write(new_file) #the new file is gonna use file writer we had before

