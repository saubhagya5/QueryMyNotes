# QueryMyNotes

**QueryMyNotes** is an AI-powered PDF chatbot that lets you ask questions and get answers from the content of multiple PDF files. It combines LangChain, OpenAI embeddings, and Streamlit to deliver a simple interactive experience.

## Tech Stack

- **Python** — Core programming language  
- **Streamlit** — For building the web interface  
- **LangChain** — For chaining LLMs and retrieval  
- **OpenAI Embeddings** — For semantic document indexing  
- **FAISS** — Vector store for fast similarity search  
- **PyPDF2** — To extract text from PDF files  
- **dotenv** — For environment variable management  

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Create a .env file with your OpenAI API key
# Example:
# OPENAI_API_KEY=your_api_key_here

# Start the Streamlit app
streamlit run app.py
