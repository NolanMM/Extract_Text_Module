# Text Extraction Module (Python -  PDF - Image)

This repository contains code examples for extracting text from PDF or Images files using Python.

## Prerequisites

Before running the code examples, make sure you have the following dependencies installed:

- [PyPDF2](https://pypi.org/project/PyPDF2/): A Python library for reading and extracting text from PDF files. You can install it via pip:
  
  ```
  pip install PyPDF2
  ```
- [pytesseract](https://github.com/UB-Mannheim/tesseract/wiki): : A Python wrapper for Google's Tesseract-OCR Engine. You can install it via pip:

  ```
  pip install pytesseract
  ```
- [Tesseract-OCR Engine](https://github.com/UB-Mannheim/tesseract/wiki): Optical Character Recognition (OCR) software for recognizing text in images. Download and install it from the official repository.
  ```
  @QuickLink: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
  ```

## Usage

To use the code examples in this repository, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/pdf-text-extraction.git
```

2. Install and Set Up All Prerequisites

Note: By default when we setup the Tesseract-OCR Engine, the root default will be C:\Program Files\Tesseract-OCR\tesseract.exe.
If you change the installed root, please update the ```pytesseract_path``` variable
