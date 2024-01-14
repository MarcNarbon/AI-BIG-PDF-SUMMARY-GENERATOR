import PyPDF2

def read_pdf(file_path):
    """
    Read a PDF and return its content.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Content of the PDF file.
    """
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        content = ""
        for page in range(reader.getNumPages()):
            content += reader.getPage(page).extractText()
    return content