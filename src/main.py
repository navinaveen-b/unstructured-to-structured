import pdfplumber
import pytesseract
from PIL import Image
import pandas as pd
import docx2txt
from bs4 import BeautifulSoup

def read_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def read_image(path):
    return pytesseract.image_to_string(Image.open(path))

def read_docx(path):
    return docx2txt.process(path)

def read_html(path):
    with open(path, "r",encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(),"html.parser")
        return soup.get_text(separator=" ")

def structure_text(text):
    data = []
    for line in text.split("\n"):
        line = line.strip()
        if line:
            data.append({"content": line,
                         "length": len(line)
                        })
    return pd.DataFrame(data)

def main():
    text = read_pdf("data/raw/sample.pdf")
    df = structure_text(text)
    df.to_csv("data/processed/output.csv", index=False)
    print("Data processed and saved at data/processed/output.csv")


if __name__ == "__main__":
    main()
    

