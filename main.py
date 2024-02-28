from PIL import Image
import pytesseract
from PyPDF2 import PdfReader


def read_image(img_path):
    pytesseract.pytesseract.tesseract_cmd = pytesseract_path
    print(pytesseract.image_to_string(Image.open(img_path)))


def extract_text_from_pdf(pdf_path):
    text = ''
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text


if __name__ == '__main__':
    # Set the path to the tesseract executable
    pytesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Set Image and PDF path
    img_path = r"Test.png"
    pdf_path = r"Test.pdf"
    while True:
        user_input = input("Please choose between 1.Image or 2.PDF or Quit: ").lower()
        if user_input == 'image' or user_input == '1':
            read_image(img_path)
        elif user_input == 'pdf' or user_input == '2':
            extract_text = extract_text_from_pdf(pdf_path)
            with open('extracted_text.txt', 'wb') as file:
                file.write(extract_text.encode('utf-8'))
        elif user_input == 'quit':
            break
        else:
            print("Invalid input, please try again.")
