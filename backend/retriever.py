from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

def get_answer(question: str) -> str:
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in docs])
    response = llm.invoke(
        f"Answer the question based on this context:\n\n{context}\n\nQuestion: {question}"
    )
    return response.content

if __name__ == "__main__":
    answer = get_answer("What is this document about?")
    print(answer)