import os
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    pdf_directory = "pdf_dir"  # Replace with the path to your PDF files directory
    docx_directory = "docx_dir"  # Replace with the path where you want to save the DOCX files

    # Create the output directory if it doesn't exist
    os.makedirs(docx_directory, exist_ok=True)

    for pdf_filename in os.listdir(pdf_directory):
        if pdf_filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, pdf_filename)
            docx_filename = pdf_filename.replace(".pdf", ".docx")
            docx_path = os.path.join(docx_directory, docx_filename)

            convert_pdf_to_docx(pdf_path, docx_path)

