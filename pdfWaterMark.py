import PyPDF2

template = PyPDF2.PdfFileReader(open('output/merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('samples/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('output/watermark_output.pdf', 'wb') as file:
		output.write(file)