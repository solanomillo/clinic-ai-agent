from langchain_google_genai import ChatGoogleGenerativeAI

def cargar_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    return llm