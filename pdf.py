import PyPDF2

#rb - read binary
with open('./samples/dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	number_of_pages = reader.getNumPages()
	writer = PyPDF2.PdfFileWriter()
	for page_number in range(number_of_pages):
		page = reader.getPage(0)
		page_content = page.extractText()
		print(page_content)
		page.rotateCounterClockwise(90)
		writer.addPage(page_content)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)
