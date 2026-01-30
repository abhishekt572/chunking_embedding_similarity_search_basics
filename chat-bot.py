import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_chroma import Chroma
from langchain_core.documents import Document

print(st.__version__)


st.header("My First Chat Bot")

with st.sidebar:
    st.title("Your Document")
    file = st.file_uploader("Upload a pdf file", type="pdf")
    chunks = ""
    
    if file is not None:
        # st.write(file)
        text = ""
        for pages in PdfReader(file).pages:
            text=text+pages.extract_text()
        # create chunks    
        text_splitter = RecursiveCharacterTextSplitter(
            separators="\n",
            chunk_size=400, 
            chunk_overlap=100)
        chunks = text_splitter.split_text(text)

# for i in range(len(chunks)):
#     st.write("chunk is of the index : ", i)
#     st.write(chunks[i])
st.write("Chunks:", len(chunks))

# API key (as requested: kept in code for now)
os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY_YOUR"
# st.write(os.getcwd())
persist_directory = os.path.join(os.getcwd(), "chroma_db")
collection_name = "pdf_chunks"

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_db = None

# Create/update the vector DB only when we have a PDF and chunks.
if file is not None and chunks:
    docs = [
        Document(
            page_content=chunk,
            metadata={
                "source": getattr(file, "name", "uploaded.pdf"),
                "chunk_index": i,
            },
        )
        for i, chunk in enumerate(chunks)
    ]

    # Persist vectors locally (Chroma).
    # Note: this recreates the collection on each upload; if you want to accumulate
    # multiple PDFs, we can switch to `add_documents` with stable IDs.
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )
    st.success(f"Stored {len(docs)} chunks in vector DB at `{persist_directory}`.")
else:
    # If a DB already exists from a previous run, you can still query it.
    vector_db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name=collection_name,
    )

# user semantic search query
user_question = st.text_input("Please enter your query")
if user_question:
    st.write("You asked:", user_question)
    k = 1
    results = vector_db.similarity_search_with_score(user_question, k=k)

    if not results:
        st.warning("No results found.")
    else:
        st.subheader("Top matches")
        for rank, (doc, score) in enumerate(results, start=1):
            st.markdown(
                f"**{rank}. score:** `{score}`  \n"
                f"**chunk_index:** `{doc.metadata.get('chunk_index')}`  \n"
                f"**source:** `{doc.metadata.get('source')}`"
            )
            st.write(doc.page_content)

