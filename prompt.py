from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system",
         "Kamu adalah AI diagnostik komputer dengan memory percakapan. "
         "Kamu HARUS menggunakan history chat untuk memahami konteks sebelumnya. "
         "Jika informasi kurang, ajukan pertanyaan lanjutan."),

        ("human",
         "Input terbaru: {question}\n\n"
         "Konteks (memory + RAG): {context}\n\n"
         "Berikan analisa lengkap dan lanjutkan percakapan secara natural.")
    ])