import pdfplumber
import nltk
import re
import string
import os


nltk.download("punkt")


def extract_and_tokenize(input_file):
    ext = input_file.rsplit(".", 1)[-1].lower()
    base_name = os.path.splitext(input_file)[0]  
    output_file = f"{base_name}_tokens.txt"  
    text = ""

    
    if ext == "txt":
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

    
    elif ext == "pdf":
        with pdfplumber.open(input_file) as pdf:
            for page in pdf.pages:
                extracted_page_text = page.extract_text()
                if extracted_page_text:
                    text += extracted_page_text + " "   

    else:
        raise ValueError("Unsupported file format. Only TXT and PDF are allowed.")

    
    text = re.sub(r"\s+", " ", text)  
    tokens = nltk.word_tokenize(text)  
    tokens = [word for word in tokens if word not in string.punctuation]

    
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(tokens))  

    print(f"Tokens have been saved to {output_file}")



extract_and_tokenize("file.txt")  
extract_and_tokenize("file2.pdf")  



