import pdfplumber

def extract_pdf_content(pdf_path):
    """Extracts text from each page of the PDF."""
    content = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                content.append({"page_number": page_num, "content": text})
    return content
