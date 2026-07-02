import pandas as pd
from pypdf import PdfReader


def extract_text(uploaded_file):

    extension = uploaded_file.name.split(".")[-1].lower()

    text = ""

    if extension == "pdf":

        pdf = PdfReader(uploaded_file)

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    elif extension == "txt":

        text = uploaded_file.read().decode("utf-8")

    elif extension == "csv":

        df = pd.read_csv(uploaded_file)

        text = df.to_string(index=False)

    return text