import pandas as pd
from langchain_core.documents import Document

def load_csv():
    df = pd.read_csv("data/kerusakan.csv")

    docs = []

    for _, row in df.iterrows():
        content = f"""
Gejala: {row['gejala']}
Kerusakan: {row['kerusakan']}
Solusi: {row['solusi']}
Referensi Jurnal: {row['jurnal']}
"""

        docs.append(Document(page_content=content))

    return docs