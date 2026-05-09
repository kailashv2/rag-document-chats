from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

def get_answer(question: str) -> str:
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    )
    result = qa_chain.invoke({"query": question})
    return result["result"]

if __name__ == "__main__":
    answer = get_answer("What is this document about?")
    print(answer)