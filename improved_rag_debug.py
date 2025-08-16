#!/usr/bin/env python3
"""
Improved RAG Chain with Debugging Capabilities
This script helps identify and fix issues with the RAG chain implementation.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Load environment variables
load_dotenv()

def setup_components():
    """Setup all RAG components with improved configurations."""
    
    # 1. Initialize LLM with better model for RAG
    llm = ChatGroq(
        model="llama3-8b-8192",  # Better for RAG tasks
        temperature=0.1  # Lower temperature for more consistent answers
    )
    
    # 2. Initialize embedding model
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
    
    # 3. Load documents
    dir_path = os.path.join(os.getcwd(), "notebook", "data")
    dir_loader = DirectoryLoader(dir_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = dir_loader.load()
    print(f"Loaded {len(docs)} documents")
    
    # 4. Improved text splitting
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Increased from 500 for better context
        chunk_overlap=200,  # Increased overlap
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]  # Better separators
    )
    
    split_docs = text_splitter.split_documents(docs)
    print(f"Split into {len(split_docs)} chunks")
    
    # 5. Create vector store
    vectordb = FAISS.from_documents(split_docs, embedding_model)
    
    return llm, embedding_model, vectordb, split_docs

def create_improved_prompt():
    """Create an improved prompt template."""
    
    improved_prompt_template = """
You are a helpful AI assistant. Answer the question based on the context provided below.
If the context does not contain sufficient information to answer the question accurately, respond with:
"I do not have enough information to answer this question accurately."

Guidelines:
- Use only the information provided in the context
- Be specific and detailed in your response
- If the context contains relevant data, cite it appropriately
- If the question is not addressed in the context, say so clearly
- Provide a comprehensive answer based on the available context

Context: {context}

Question: {question}

Answer:"""
    
    return PromptTemplate(template=improved_prompt_template, input_variables=["context", "question"])

def format_docs(docs):
    """Format documents for the prompt."""
    return "\n\n".join([doc.page_content for doc in docs])

def debug_rag_chain(question, vectordb, llm, prompt):
    """Debug the RAG chain step by step."""
    
    print("=" * 80)
    print("RAG CHAIN DEBUG")
    print("=" * 80)
    print(f"Question: {question}")
    
    # 1. Test retrieval
    print("\n1. TESTING RETRIEVAL")
    print("-" * 40)
    
    # Try different retriever configurations
    retriever_configs = [
        {"k": 3, "search_type": "similarity"},
        {"k": 5, "search_type": "similarity"},
        {"k": 7, "search_type": "similarity"},
        {"k": 3, "search_type": "mmr"}  # Maximum Marginal Relevance
    ]
    
    for i, config in enumerate(retriever_configs):
        print(f"\nRetriever config {i+1}: {config}")
        retriever = vectordb.as_retriever(**config)
        retrieved_docs = retriever.get_relevant_documents(question)
        
        print(f"  Retrieved {len(retrieved_docs)} documents")
        if retrieved_docs:
            print(f"  First doc preview: {retrieved_docs[0].page_content[:200]}...")
            print(f"  Source: {retrieved_docs[0].metadata.get('source', 'Unknown')}")
    
    # 2. Test with best configuration
    print("\n2. USING OPTIMAL CONFIGURATION")
    print("-" * 40)
    
    best_retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )
    
    retrieved_docs = best_retriever.get_relevant_documents(question)
    print(f"Retrieved {len(retrieved_docs)} documents")
    
    # Show all retrieved documents
    for i, doc in enumerate(retrieved_docs):
        print(f"\nDocument {i+1}:")
        print(f"  Content: {doc.page_content[:300]}...")
        print(f"  Source: {doc.metadata.get('source', 'Unknown')}")
        print(f"  Page: {doc.metadata.get('page', 'Unknown')}")
    
    # 3. Test prompt formatting
    print("\n3. TESTING PROMPT FORMATTING")
    print("-" * 40)
    
    formatted_context = format_docs(retrieved_docs)
    print(f"Formatted context length: {len(formatted_context)} characters")
    print(f"Context preview: {formatted_context[:500]}...")
    
    # 4. Test LLM response
    print("\n4. TESTING LLM RESPONSE")
    print("-" * 40)
    
    # Create the RAG chain
    rag_chain = (
        {"context": best_retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    try:
        answer = rag_chain.invoke(question)
        print("SUCCESS! Generated answer:")
        print(answer)
        return answer
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def test_different_questions():
    """Test the RAG chain with different types of questions."""
    
    test_questions = [
        "can you tell me how Reward Modeling works?",
        "What is LoRA?",
        "What are the main findings in the Llama 2 paper?",
        "How does fine-tuning work?",
        "What are the benchmark results?"
    ]
    
    print("Setting up components...")
    llm, embedding_model, vectordb, split_docs = setup_components()
    prompt = create_improved_prompt()
    
    print("\nTesting different questions...")
    for question in test_questions:
        print(f"\n{'='*60}")
        print(f"Testing: {question}")
        print(f"{'='*60}")
        debug_rag_chain(question, vectordb, llm, prompt)

if __name__ == "__main__":
    test_different_questions() 