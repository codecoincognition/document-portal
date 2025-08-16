# Document Portal 🚀

A comprehensive document processing and analysis platform built with FastAPI, LangChain, and modern AI technologies. This portal provides document ingestion, analysis, comparison, and conversational AI capabilities for document-based workflows.

## ✨ Features

### 🔍 Document Analysis
- **PDF Processing**: Extract and analyze text from PDF documents
- **Content Analysis**: AI-powered document content analysis and insights
- **Multi-format Support**: Handle PDF, DOCX, and other document formats

### 📊 Document Comparison
- **Side-by-side Analysis**: Compare reference and actual documents
- **LLM-powered Comparison**: Use AI models to identify differences and similarities
- **Structured Results**: Get comparison results in organized, tabular format

### 💬 Conversational AI (RAG)
- **Document Indexing**: Build searchable indexes from multiple documents
- **Intelligent Retrieval**: FAISS-based vector search with configurable parameters
- **Conversational Interface**: Chat with your documents using natural language
- **Session Management**: Maintain conversation context across multiple queries

### 🏗️ Architecture
- **FastAPI Backend**: Modern, fast web framework with automatic API documentation
- **LangChain Integration**: Leverage multiple LLM providers (Groq, Gemini, OpenAI)
- **Vector Database**: FAISS for efficient similarity search
- **Modular Design**: Clean separation of concerns with dedicated modules

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Conda or Python virtual environment
- API keys for your chosen LLM providers

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/codecoincognition/document-portal.git
cd document-portal
```

2. **Create and activate conda environment**
```bash
# Create environment
conda create -p env python=3.10 -y

# Activate environment (use full path)
conda activate /Users/vikassah/Documents/code/krish-naik-llm-ops/document-portal/env
```

3. **Install dependencies**
```bash
# Install using conda for better compatibility
conda install -c conda-forge fastapi uvicorn python-multipart python-dotenv -y

# Install remaining packages
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API keys
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

5. **Run the application**
```bash
# Development mode with auto-reload
uvicorn api.main:app --host 0.0.0.0 --port 8080 --reload

# Production mode
uvicorn api.main:app --host 0.0.0.0 --port 8080
```

## 🌐 API Endpoints

### Health Check
- **GET** `/health` - Service health status

### Document Analysis
- **POST** `/analyze` - Analyze a single document
  - **Body**: `file` (UploadFile) - Document to analyze
  - **Returns**: Analysis results and insights

### Document Comparison
- **POST** `/compare` - Compare two documents
  - **Body**: 
    - `reference` (UploadFile) - Reference document
    - `actual` (UploadFile) - Document to compare against
  - **Returns**: Comparison results with session ID

### Conversational AI
- **POST** `/chat/index` - Build search index from documents
  - **Body**:
    - `files` (List[UploadFile]) - Documents to index
    - `session_id` (Optional[str]) - Session identifier
    - `use_session_dirs` (bool) - Use session-based directories
    - `chunk_size` (int) - Text chunk size (default: 1000)
    - `chunk_overlap` (int) - Chunk overlap (default: 200)
    - `k` (int) - Number of retrieved chunks (default: 5)
  - **Returns**: Session ID and indexing status

- **POST** `/chat/query` - Query documents using natural language
  - **Body**:
    - `question` (str) - Your question about the documents
    - `session_id` (Optional[str]) - Session identifier
    - `use_session_dirs` (bool) - Use session-based directories
    - `k` (int) - Number of retrieved chunks (default: 5)
  - **Returns**: AI-generated answer based on document content

## 🏗️ Project Structure

```
document-portal/
├── api/                          # FastAPI application
│   ├── main.py                  # Main API endpoints
│   └── data/                    # API-related data
├── src/                         # Core application logic
│   ├── document_analyzer/       # Document analysis functionality
│   ├── document_chat/           # Conversational AI and RAG
│   ├── document_compare/        # Document comparison logic
│   └── document_ingestion/      # Document processing and ingestion
├── static/                      # Static files (CSS, JS)
├── templates/                   # HTML templates
├── config/                      # Configuration files
├── utils/                       # Utility functions
├── tests/                       # Test files
├── requirements.txt             # Python dependencies
├── setup.py                     # Package configuration
└── .env.example                 # Environment variables template
```

## 🔧 Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for LLM access
- `GOOGLE_API_KEY`: Your Google Gemini API key
- `FAISS_BASE`: Base directory for FAISS indexes (default: "faiss_index")
- `UPLOAD_BASE`: Base directory for uploaded files (default: "data")
- `FAISS_INDEX_NAME`: Name of the FAISS index (default: "index")

### LLM Providers
The platform supports multiple LLM providers:

- **Groq** (Recommended for speed)
  - [Get API Key](https://console.groq.com/keys)
  - [Documentation](https://console.groq.com/docs/overview)

- **Google Gemini**
  - [Get API Key](https://aistudio.google.com/apikey)
  - [Documentation](https://ai.google.dev/gemini-api/docs/models)

- **OpenAI** (Paid)
- **Claude** (Paid)
- **Hugging Face** (Free)
- **Ollama** (Local setup)

## 📚 Usage Examples

### 1. Document Analysis
```bash
curl -X POST "http://localhost:8080/analyze" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"
```

### 2. Document Comparison
```bash
curl -X POST "http://localhost:8080/compare" \
  -H "Content-Type: multipart/form-data" \
  -F "reference=@reference.pdf" \
  -F "actual=@actual.pdf"
```

### 3. Build Document Index
```bash
curl -X POST "http://localhost:8080/chat/index" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@doc1.pdf" \
  -F "files=@doc2.pdf" \
  -F "session_id=my_session" \
  -F "chunk_size=1000" \
  -F "chunk_overlap=200" \
  -F "k=5"
```

### 4. Query Documents
```bash
curl -X POST "http://localhost:8080/chat/query" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "question=What are the main topics discussed in the documents?" \
  -d "session_id=my_session" \
  -d "k=5"
```

## 🧪 Testing

Run the test suite:
```bash
pytest
```

## 🚀 Deployment

### Development
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8080
```

### Production
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8080 --workers 4
```

### Docker (Coming Soon)
```bash
# Build image
docker build -t document-portal .

# Run container
docker run -p 8080:8080 document-portal
```

## 🔒 Security

- **API Key Management**: Store API keys in environment variables
- **File Upload Validation**: Secure file handling and validation
- **CORS Configuration**: Configurable cross-origin resource sharing
- **Input Sanitization**: Protect against malicious inputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs and feature requests on GitHub
- **Documentation**: Check the inline code comments and API docs
- **Community**: Join our discussions and share your use cases

## 🎯 Roadmap

- [ ] Docker containerization
- [ ] Additional LLM provider support
- [ ] Advanced document preprocessing
- [ ] Real-time collaboration features
- [ ] Mobile application
- [ ] Advanced analytics dashboard

## 🙏 Acknowledgments

- **LangChain**: For the excellent LLM orchestration framework
- **FastAPI**: For the modern, fast web framework
- **FAISS**: For efficient similarity search capabilities
- **Open Source Community**: For the amazing tools and libraries

---

**Built with ❤️ by the CodeCoincognition Team**

*For questions and support, please open an issue on GitHub.*


