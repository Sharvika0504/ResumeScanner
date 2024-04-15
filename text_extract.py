import fitz  # Playaround with different python libraries for text extract

print("PyMuPDF version:", fitz.__version__)
def extract_text_from_pdf(pdf_path):
    doc = fitz.open('Resume/SharvikaNitinKulkarni_Resume_Doorlist .pdf')  
    text = ""
    for page in doc: 
        text += page.get_text()  
    doc.close()
    return text


pdf_file_path = 'Resume/SharvikaNitinKulkarni_Resume_Doorlist.pdf'
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text)