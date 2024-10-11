---

## PDFBot.ai - AI-Powered PDF Assistant 🤖📄

**PDFBot.ai** is an AI chatbot that helps users quickly extract information and answer questions from uploaded PDF documents. Utilizing technologies like LangChain, Llama 3, and Groq API, it offers fast, accurate responses, making it perfect for users who need to analyze PDF content efficiently.

### Key Features:
- **PDF Text Extraction**: Automatically extracts the full text from uploaded PDFs for processing.
- **Conversational AI**: Users can ask questions about the PDF content and get relevant answers.
- **Groq Acceleration**: Leverages Groq hardware for faster PDF processing and reduced latency.
- **Llama 3 Model**: Integrates Llama 3 for advanced natural language understanding and accurate answers.
- **Efficient Document Search**: Uses embeddings and FAISS to retrieve and organize document chunks based on the query.

### Technologies:
- **LangChain**: Manages language models and retrieval to facilitate smooth conversation flow.
- **Groq**: Accelerates document processing for better performance.
- **Llama 3**: Powers the core AI to interpret and respond to user queries.
- **Streamlit**: Provides a simple interface for uploading PDFs and interacting with the chatbot.
- **FAISS**: Performs quick similarity searches on document chunks.

### How It Works:
1. **Upload a PDF**: Simply drag and drop the PDF file into the interface.
2. **Ask Your Question**: Type in a question related to the PDF content.
3. **Receive Instant Answers**: Get AI-powered responses based on the text within the PDF.

### Installation:
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your Groq API key in the `.env` file.
3. Run the app with Streamlit:
   ```bash
   streamlit run app.py
   ```

---

**PDFBot.ai** offers a smart and quick way to interact with PDFs using advanced AI and efficient processing technologies.
