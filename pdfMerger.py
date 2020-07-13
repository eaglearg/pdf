import PyPDF2
import sys

inputs = sys.argv[1:]  #all the arguments after 1 in a list test git again

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)
	merger.write('./output/merged.pdf')

pdf_combiner(inputs)