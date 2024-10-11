import os
from groq import Groq  # Ensure you import Groq correctly
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import streamlit as st
from dotenv import load_dotenv
import PyPDF2



load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key)


llama_llm = Ollama(model="llama3")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

# Function to process text into chunks
def process_pdf(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    documents = [Document(page_content=chunk) for chunk in chunks]
    return documents

# Setup the conversational QA chain using Groq for chat completions
def setup_chain(documents):
    embeddings = OllamaEmbeddings(model="llama3")
    db = FAISS.from_documents(documents, embeddings)
    retriever = db.as_retriever()

    # Initialize the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llama_llm,
        chain_type="stuff",
        retriever=retriever
    )
    return qa_chain

# Streamlit app
st.title("PDF Chatbot with Llama3 (Groq-Accelerated)")

# File upload
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.write("Processing PDF...")

    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)
    st.write("PDF Processed!")

    # Process text into chunks and set up LangChain
    documents = process_pdf(text)
    qa_chain = setup_chain(documents)

   
    chat_history = []

  
    question = st.text_input("Ask a question from the PDF")

    if st.button("Ask"):
        if question:
            
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": question}],
                model="llama3-8b-8192",
            )
            answer = chat_completion.choices[0].message.content
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question.")
