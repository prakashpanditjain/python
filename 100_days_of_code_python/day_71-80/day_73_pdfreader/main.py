from PyPDF2 import PdfMerger
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

pdf_path = 'python_cheat_sheet.pdf'

with open(pdf_path, 'rb'):
    reader = PdfReader(pdf_path)

    for i,page in enumerate(reader.pages):
        text = page.extract_text()
        if 'slice' in text.lower():
            print(f"Found 'slice' in page {i + 1}:")
            print(text)
            break

merged_file = './merged_pdf.pdf'
if not merged_file:
    merger = PdfMerger()
    filepath = './python_cheat_sheet.pdf'
    second_file = './syllabus_python_100days.pdf'
    merger.append(filepath)
    merger.append(second_file)
    merger.write('merged_pdf.pdf')

# split pdf with page number
reader = PdfReader('merged_pdf.pdf')
writer = PdfWriter()
for i, page in enumerate(reader.pages):

    #Split the PDF into individual pages
    # writer.add_page(page)
    # with open(f"page_{i+1}.pdf", 'wb') as f:
    #     writer.write(f)

    #Do write all 10 pages into single pdf
    if i <= 10:  # Only process pages up to page 10
        writer.add_page(page)

with open(f"first_10_pages.pdf", "wb") as f:
    writer.write(f)