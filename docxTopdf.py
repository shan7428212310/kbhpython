import os
from docx2txt import convert
def docxTopdf(docx_path):
    # Specify the path to your DOCX file
    input_path = "path/to/your/document.docx"

    # Specify the output path for the PDF file (optional)
    output_path = "path/to/your/output/document.pdf"

    # Convert the DOCX to PDF
    convert(input_path, output_path)

    # Delete the DOCX file after conversion
    if os.path.exists(input_path):
        os.remove(input_path)
        print(f"{input_path} has been deleted.")
    else:
        print(f"The file {input_path} does not exist.")
