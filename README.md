# PDF Chat Bot

A simple Streamlit app that lets you upload a PDF, chunk its text, store it in a local vector database (Chroma), and run **semantic search** over it using Google Gemini embeddings.

## Features

- **PDF upload** – Upload a PDF from the sidebar.
- **Text chunking** – Extracts text from all pages and splits it into overlapping chunks (configurable size/overlap).
- **Vector store** – Embeds chunks with [Google Gemini](https://ai.google.dev/) and stores them in [Chroma](https://www.trychroma.com/) on disk.
- **Semantic search** – Type a question; the app finds the most relevant chunk(s) by similarity and shows them with scores.

## Prerequisites

- **Python** 3.9 or higher
- **Google AI API key** – Get one from [Google AI Studio](https://aistudio.google.com/apikey)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/abhishekt572/chunking_embedding_similarity_search_basics.git
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Google API key**

   Set the `GOOGLE_API_KEY` environment variable (do **not** commit your key to the repo):

   **Windows (PowerShell)**

   ```powershell
   $env:GOOGLE_API_KEY = "your-api-key-here"
   ```

   **Windows (CMD)**

   ```cmd
   set GOOGLE_API_KEY=your-api-key-here
   ```

   **macOS / Linux**

   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

   Or create a `.env` file in the project root and load it with a package like `python-dotenv` (not included in the default setup).

## Running the app

```bash
streamlit run chat-bot.py
```

The app will open in your browser (usually `http://localhost:8501`).

## Usage

1. In the **sidebar**, upload a PDF file.
2. Wait until the app shows that chunks were stored in the vector DB.
3. In the main area, type your question in **"Please enter your query"**.
4. The app will show the top matching chunk(s) with similarity score, chunk index, and source file.

## Project structure

```
create-chat/
├── chat-bot.py          # Main Streamlit app
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── chroma_db/           # Local Chroma DB (created after first PDF upload)
```

## Dependencies

- **Streamlit** – Web UI
- **PyPDF2** – PDF text extraction
- **LangChain** – Text splitting, embeddings, Chroma integration
- **langchain-google-genai** – Google Gemini embeddings
- **langchain-chroma** / **chromadb** – Vector store

See `requirements.txt` for versions.

## License

MIT (or your preferred license). Feel free to use and modify for personal or educational use.

## Contributing

Issues and pull requests are welcome. For major changes, open an issue first to discuss.
