from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

def ingest_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )
    print(f"✅ Ingested {len(chunks)} chunks from {pdf_path}")

if __name__ == "__main__":
    ingest_pdf("../docs/test.pdf")