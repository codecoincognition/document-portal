# Document Portal Architecture 🏗️

This document provides a comprehensive overview of the Document Portal system architecture, including component design, data flow, and technical decisions.

## 🎯 System Overview

The Document Portal is a microservices-based document processing platform that leverages modern AI technologies to provide document analysis, comparison, and conversational AI capabilities. The system is built with a modular, scalable architecture that separates concerns and enables easy extension.

## 🏛️ High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Layer                             │
├─────────────────────────────────────────────────────────────────┤
│  Web UI (HTML/CSS/JS)  │  API Clients  │  Mobile Apps        │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API Gateway Layer                          │
├─────────────────────────────────────────────────────────────────┤
│                    FastAPI Application                         │
│              (api/main.py - Main Router)                      │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Business Logic Layer                        │
├─────────────────────────────────────────────────────────────────┤
│  Document    │  Document    │  Document    │  Document        │
│  Analyzer    │  Comparator  │  Chat        │  Ingestion      │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AI/ML Layer                               │
├─────────────────────────────────────────────────────────────────┤
│  LangChain   │  LLM         │  Embedding   │  Vector          │
│  Framework   │  Providers   │  Models      │  Search          │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Data Layer                                │
├─────────────────────────────────────────────────────────────────┤
│  File        │  FAISS       │  Temporary   │  Configuration  │
│  Storage     │  Indexes     │  Storage     │  Files          │
└─────────────────────────────────────────────────────────────────┘
```

## 🔧 Core Components

### 1. API Gateway Layer

#### FastAPI Application (`api/main.py`)
- **Purpose**: Central routing and request handling
- **Responsibilities**:
  - Request validation and routing
  - CORS management
  - Static file serving
  - Template rendering
  - Error handling and logging

#### Key Features:
- **CORS Middleware**: Configurable cross-origin resource sharing
- **Static Files**: Serves CSS, JavaScript, and other static assets
- **Template Engine**: Jinja2 templates for dynamic HTML generation
- **File Upload Handling**: Multipart form data processing

### 2. Business Logic Layer

#### Document Analyzer (`src/document_analyzer/`)
```python
class DocumentAnalyzer:
    """
    Analyzes document content using AI models
    - Text extraction and preprocessing
    - Content analysis and insights
    - Structured result generation
    """
```

**Responsibilities**:
- PDF text extraction and processing
- Content analysis using LLM models
- Insight generation and summarization
- Result formatting and structuring

#### Document Comparator (`src/document_compare/`)
```python
class DocumentComparator:
    """
    Compares two documents and identifies differences
    - File management and storage
    - Text extraction and normalization
    - LLM-powered comparison analysis
    """
```

**Responsibilities**:
- Document pair management
- Text extraction and preprocessing
- LLM-based comparison analysis
- Result tabulation and formatting

#### Document Chat (`src/document_chat/`)
```python
class ConversationalRAG:
    """
    Retrieval-Augmented Generation for document Q&A
    - Document indexing and vectorization
    - Semantic search and retrieval
    - Conversational AI responses
    """
```

**Responsibilities**:
- Document indexing and vectorization
- FAISS-based similarity search
- RAG chain orchestration
- Conversation context management

#### Document Ingestion (`src/document_ingestion/`)
```python
class DocHandler:
    """
    Handles document upload, storage, and processing
    - File format validation
    - Storage management
    - Text extraction pipeline
    """
```

**Responsibilities**:
- File upload and validation
- Storage management
- Text extraction pipeline
- Session management

### 3. AI/ML Layer

#### LangChain Integration
- **Framework**: LangChain 0.3.27
- **Purpose**: LLM orchestration and chain management
- **Components**:
  - Document loaders and processors
  - Text splitters and chunking
  - Vector store integration
  - RAG chain construction

#### LLM Providers
```python
# Supported LLM Providers
langchain_groq==0.3.6          # Groq (Fast, Free tier)
langchain_google_genai==2.1.8   # Google Gemini
# Extensible for OpenAI, Claude, Hugging Face, Ollama
```

#### Vector Search (FAISS)
- **Purpose**: Efficient similarity search and retrieval
- **Features**:
  - In-memory and on-disk storage
  - Configurable similarity metrics
  - Session-based index management
  - Scalable vector operations

### 4. Data Layer

#### File Storage Structure
```
document-portal/
├── data/                    # Uploaded documents
│   └── {session_id}/       # Session-based organization
├── faiss_index/            # Vector search indexes
│   └── {session_id}/       # Session-based indexes
├── logs/                    # Application logs
├── config/                  # Configuration files
└── static/                  # Static assets
```

#### FAISS Index Management
```python
class FaissManager:
    """
    Manages FAISS vector indexes
    - Index creation and storage
    - Similarity search operations
    - Session-based organization
    """
```

## 🔄 Data Flow

### 1. Document Analysis Flow
```
User Upload → File Validation → Text Extraction → AI Analysis → Structured Results
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
  FastAPI      DocHandler     PyMuPDF      LangChain      JSON Response
  Endpoint     Validation     Processing    LLM Chain     to Client
```

### 2. Document Comparison Flow
```
Two Files → File Storage → Text Extraction → LLM Comparison → Tabular Results
    │           │              │              │              │
    ▼           ▼              ▼              ▼              ▼
  Upload    Session Dir    Combined Text   AI Analysis    DataFrame
  Endpoint   Management    Processing      Comparison     Response
```

### 3. Conversational AI Flow
```
Documents → Indexing → Vector Storage → Query → Retrieval → RAG → Response
    │          │           │           │        │          │      │
    ▼          ▼           ▼           ▼        ▼          ▼      ▼
  Upload    Chunking   FAISS Index  User    Similarity  LLM    AI
  Files     & Embed    Storage      Query   Search      Chain  Answer
```

## 🏗️ Technical Design Decisions

### 1. Modular Architecture
- **Separation of Concerns**: Each module handles specific functionality
- **Loose Coupling**: Modules communicate through well-defined interfaces
- **High Cohesion**: Related functionality grouped together
- **Easy Testing**: Isolated components for unit testing

### 2. Session Management
- **Session IDs**: Unique identifiers for document processing sessions
- **Directory Organization**: Session-based file and index organization
- **State Persistence**: Maintains context across multiple operations
- **Cleanup**: Automatic cleanup of temporary files

### 3. Vector Search Strategy
- **FAISS Choice**: Fast, scalable similarity search
- **Chunking Strategy**: Configurable text chunking with overlap
- **Embedding Models**: Support for multiple embedding providers
- **Index Persistence**: On-disk storage for large document collections

### 4. Error Handling
- **Graceful Degradation**: System continues operation on non-critical errors
- **Detailed Logging**: Comprehensive error logging for debugging
- **User Feedback**: Clear error messages for end users
- **Recovery Mechanisms**: Automatic retry and fallback strategies

## 🔌 Integration Points

### 1. External APIs
- **LLM Providers**: REST API integration for AI models
- **File Storage**: Local filesystem with cloud storage potential
- **Authentication**: Extensible authentication system

### 2. Internal Communication
- **Module Interfaces**: Well-defined contracts between components
- **Data Contracts**: Structured data exchange formats
- **Event System**: Asynchronous event handling (future enhancement)

## 📊 Performance Characteristics

### 1. Scalability
- **Horizontal Scaling**: Stateless API design enables load balancing
- **Vertical Scaling**: Configurable worker processes
- **Resource Management**: Efficient memory and CPU utilization

### 2. Response Times
- **Document Analysis**: 2-5 seconds for typical documents
- **Document Comparison**: 5-10 seconds for document pairs
- **Chat Queries**: 1-3 seconds for indexed documents
- **Indexing**: 10-30 seconds depending on document size

### 3. Resource Usage
- **Memory**: 100MB-1GB depending on document size
- **CPU**: Moderate usage during processing, low during idle
- **Storage**: Configurable based on document retention needs

## 🔒 Security Considerations

### 1. File Security
- **Upload Validation**: File type and size restrictions
- **Path Traversal**: Prevention of directory traversal attacks
- **Temporary Storage**: Secure handling of uploaded files

### 2. API Security
- **Input Validation**: Comprehensive input sanitization
- **Rate Limiting**: Configurable request rate limits
- **CORS Configuration**: Secure cross-origin resource sharing

### 3. Data Privacy
- **API Key Management**: Secure storage of external API keys
- **Session Isolation**: User session data separation
- **Logging**: Privacy-conscious logging practices

## 🚀 Deployment Architecture

### 1. Development Environment
```
Local Machine → Conda Environment → FastAPI Dev Server → Local Storage
```

### 2. Production Environment
```
Load Balancer → Multiple API Instances → Shared Storage → Monitoring
```

### 3. Container Strategy (Future)
```
Docker Containers → Kubernetes Orchestration → Cloud Storage → Auto-scaling
```

## 🔮 Future Architecture Enhancements

### 1. Microservices Evolution
- **Service Decomposition**: Break into smaller, focused services
- **Message Queues**: Asynchronous processing with Redis/RabbitMQ
- **API Gateway**: Advanced routing and rate limiting

### 2. Cloud Integration
- **Cloud Storage**: S3-compatible object storage
- **Managed Databases**: PostgreSQL for metadata, Redis for caching
- **Serverless Functions**: Event-driven processing

### 3. Advanced AI Features
- **Multi-modal Processing**: Image and text analysis
- **Real-time Collaboration**: WebSocket-based live updates
- **Advanced Analytics**: Document insights and trends

## 📋 Architecture Checklist

- [x] **Modular Design**: Clear separation of concerns
- [x] **API-First**: RESTful API design
- [x] **Scalable**: Horizontal and vertical scaling support
- [x] **Secure**: Input validation and security measures
- [x] **Testable**: Unit and integration test support
- [x] **Documented**: Comprehensive code and API documentation
- [x] **Configurable**: Environment-based configuration
- [x] **Logging**: Comprehensive logging and monitoring
- [ ] **Metrics**: Performance and health monitoring
- [ ] **Caching**: Redis-based caching layer
- [ ] **Queue System**: Asynchronous job processing
- [ ] **Load Balancing**: Multiple instance support
- [ ] **Auto-scaling**: Dynamic resource allocation

---

## 📚 Related Documentation

- [README.md](./README.md) - Project overview and setup
- [API Documentation](./api/) - Detailed API specifications
- [Configuration Guide](./config/) - Environment and system configuration
- [Testing Guide](./tests/) - Testing strategies and examples

---

*This architecture document is maintained by the CodeCoincognition Team. For questions or suggestions, please open an issue on GitHub.*
