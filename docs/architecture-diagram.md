# Document Portal - Visual Architecture Diagrams 📊

This document contains visual representations of the Document Portal architecture using Mermaid diagrams.

## 🏗️ System Architecture Overview

```mermaid
graph TB
    subgraph "Client Layer"
        A[Web UI] 
        B[API Clients]
        C[Mobile Apps]
    end
    
    subgraph "API Gateway Layer"
        D[FastAPI Application]
        E[CORS Middleware]
        F[Static File Server]
    end
    
    subgraph "Business Logic Layer"
        G[Document Analyzer]
        H[Document Comparator]
        I[Document Chat]
        J[Document Ingestion]
    end
    
    subgraph "AI/ML Layer"
        K[LangChain Framework]
        L[LLM Providers]
        M[Embedding Models]
        N[Vector Search]
    end
    
    subgraph "Data Layer"
        O[File Storage]
        P[FAISS Indexes]
        Q[Configuration]
        R[Logs]
    end
    
    A --> D
    B --> D
    C --> D
    
    D --> E
    D --> F
    D --> G
    D --> H
    D --> I
    D --> J
    
    G --> K
    H --> K
    I --> K
    J --> K
    
    K --> L
    K --> M
    K --> N
    
    G --> O
    H --> O
    I --> P
    J --> O
    
    K --> Q
    D --> R
```

## 🔄 Data Flow Diagrams

### Document Analysis Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as FastAPI
    participant D as DocHandler
    participant P as PyMuPDF
    participant L as LangChain
    participant AI as LLM
    
    U->>F: Upload PDF
    F->>D: Process File
    D->>P: Extract Text
    P->>D: Return Text
    D->>L: Analyze Content
    L->>AI: Process with LLM
    AI->>L: Return Analysis
    L->>F: Structured Results
    F->>U: JSON Response
```

### Document Comparison Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as FastAPI
    participant DC as DocumentComparator
    participant L as LangChain
    participant AI as LLM
    
    U->>F: Upload Two Files
    F->>DC: Process Files
    DC->>DC: Extract & Combine Text
    DC->>L: Compare Documents
    L->>AI: LLM Analysis
    AI->>L: Comparison Results
    L->>F: Tabular Data
    F->>U: DataFrame Response
```

### Conversational AI Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as FastAPI
    participant CI as ChatIngestor
    participant FAISS as FAISS Index
    participant RAG as RAG Chain
    participant AI as LLM
    
    U->>F: Upload Documents
    F->>CI: Index Documents
    CI->>CI: Chunk & Embed
    CI->>FAISS: Store Vectors
    
    U->>F: Ask Question
    F->>FAISS: Search Similar
    FAISS->>RAG: Return Chunks
    RAG->>AI: Generate Answer
    AI->>RAG: AI Response
    RAG->>F: Final Answer
    F->>U: AI Response
```

## 🏛️ Component Architecture

### Core Modules Structure

```mermaid
graph LR
    subgraph "API Layer"
        A[main.py]
    end
    
    subgraph "Core Modules"
        B[document_analyzer]
        C[document_compare]
        D[document_chat]
        E[document_ingestion]
    end
    
    subgraph "Utilities"
        F[config_loader]
        G[document_ops]
        H[file_io]
        I[model_loader]
    end
    
    subgraph "External Dependencies"
        J[LangChain]
        K[FAISS]
        L[FastAPI]
        M[PyMuPDF]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    
    B --> F
    C --> F
    D --> F
    E --> F
    
    B --> G
    C --> G
    D --> G
    E --> G
    
    B --> H
    C --> H
    D --> H
    E --> H
    
    B --> I
    C --> I
    D --> I
    E --> I
    
    I --> J
    D --> K
    A --> L
    E --> M
```

## 🔌 Integration Architecture

### LLM Provider Integration

```mermaid
graph TB
    subgraph "Document Portal"
        A[LangChain Interface]
        B[Model Loader]
        C[Provider Selection]
    end
    
    subgraph "LLM Providers"
        D[Groq API]
        E[Google Gemini]
        F[OpenAI]
        G[Claude]
        H[Hugging Face]
        I[Ollama]
    end
    
    A --> B
    B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    C --> H
    C --> I
```

### Storage Architecture

```mermaid
graph TB
    subgraph "Application"
        A[Document Portal]
    end
    
    subgraph "Local Storage"
        B[data/]
        C[faiss_index/]
        D[logs/]
        E[config/]
    end
    
    subgraph "Future Cloud Storage"
        F[S3 Compatible]
        G[PostgreSQL]
        H[Redis Cache]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    
    A -.-> F
    A -.-> G
    A -.-> H
```

## 🚀 Deployment Architecture

### Development Environment

```mermaid
graph LR
    A[Developer Machine] --> B[Conda Environment]
    B --> C[FastAPI Dev Server]
    C --> D[Local Storage]
    C --> E[Local FAISS]
```

### Production Environment

```mermaid
graph TB
    subgraph "Load Balancer"
        A[NGINX/HAProxy]
    end
    
    subgraph "Application Instances"
        B[Instance 1]
        C[Instance 2]
        D[Instance N]
    end
    
    subgraph "Shared Storage"
        E[Shared File Storage]
        F[Shared FAISS Indexes]
        G[Database]
    end
    
    subgraph "Monitoring"
        H[Logs]
        I[Metrics]
        J[Health Checks]
    end
    
    A --> B
    A --> C
    A --> D
    
    B --> E
    B --> F
    B --> G
    C --> E
    C --> F
    C --> G
    D --> E
    D --> F
    D --> G
    
    B --> H
    C --> H
    D --> H
```

### Future Container Architecture

```mermaid
graph TB
    subgraph "Kubernetes Cluster"
        A[Ingress Controller]
        B[API Gateway]
        C[Document Portal Pods]
        D[Worker Pods]
    end
    
    subgraph "Storage Layer"
        E[Persistent Volumes]
        F[Object Storage]
        G[Database]
    end
    
    subgraph "Monitoring"
        H[Prometheus]
        I[Grafana]
        J[ELK Stack]
    end
    
    A --> B
    B --> C
    B --> D
    
    C --> E
    C --> F
    C --> G
    D --> E
    D --> F
    
    C --> H
    D --> H
    H --> I
    H --> J
```

## 📊 Performance Metrics

### Response Time Distribution

```mermaid
graph LR
    A[Document Analysis<br/>2-5s] --> B[Fast Response]
    C[Document Comparison<br/>5-10s] --> D[Medium Response]
    E[Document Indexing<br/>10-30s] --> F[Slow Response]
    G[Chat Queries<br/>1-3s] --> H[Very Fast Response]
```

### Resource Usage Patterns

```mermaid
graph TB
    subgraph "Memory Usage"
        A[Idle: 100MB]
        B[Processing: 500MB]
        C[Large Docs: 1GB+]
    end
    
    subgraph "CPU Usage"
        D[Idle: 5%]
        E[Processing: 60%]
        F[Peak: 90%]
    end
    
    subgraph "Storage"
        G[Small Docs: 10MB]
        H[Medium Docs: 100MB]
        I[Large Docs: 1GB+]
    end
```

---

## 📝 Diagram Notes

- **Solid Lines**: Direct dependencies and data flow
- **Dashed Lines**: Future/planned integrations
- **Subgraphs**: Logical grouping of related components
- **Colors**: Different colors represent different layers (when rendered)

## 🔧 Rendering

These diagrams can be rendered in:
- **GitHub**: Native Mermaid support
- **GitLab**: Native Mermaid support
- **VS Code**: Mermaid extension
- **Online**: [Mermaid Live Editor](https://mermaid.live/)

---

*These diagrams are maintained by the CodeCoincognition Team. For updates or corrections, please open an issue on GitHub.*
