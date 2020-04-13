import PyPDF2
import sys
import os

inputs = sys.argv[1:] #takes all more than just two PDF files

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

pdf_combiner(inputs)