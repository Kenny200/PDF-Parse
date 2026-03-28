# First, install PyPDF2 if you haven't
# pip install PyPDF2

import PyPDF2
import os

pdf_path = os.path.expanduser('~/PHYS203/PHYS203day1.pdf')

# Open the PDF file
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    
    # Loop through all pages
    for page in reader.pages:
        text += page.extract_text() + '\n'

print(text)
