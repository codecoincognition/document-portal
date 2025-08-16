#!/usr/bin/env python3
"""
Quick Fixes for RAG Chain Issues
This script addresses the specific problems in the current RAG implementation.
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

def fix_rag_chain():
    """Fix the RAG chain with the identified issues."""
    
    print("🔧 Fixing RAG Chain Issues...")
    
    # Issue 1: Fix the typo in prompt template
    print("\n1. Fixing prompt template typo...")
    fixed_prompt_template = """
Answer the question based on the context provided below.
If the context does not contain sufficient information, respond with:
"I do not have enough information to answer this question"

Context: {context}

Question: {question}

Answer:"""
    
    # Issue 2: Use better LLM model for RAG
    print("2. Using better LLM model...")
    llm = ChatGroq(
        model="llama3-8b-8192",  # Better for RAG than deepseek-r1-distill-llama-70b
        temperature=0.1  # Lower temperature for more consistent answers
    )
    
    # Issue 3: Better text splitting
    print("3. Improving text splitting...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Increased from 500
        chunk_overlap=200,  # Increased from 150
        length_function=len
    )
    
    # Issue 4: Load documents
    print("4. Loading documents...")
    dir_path = os.path.join(os.getcwd(), "notebook", "data")
    dir_loader = DirectoryLoader(dir_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = dir_loader.load()
    print(f"   Loaded {len(docs)} documents")
    
    # Issue 5: Better chunking
    split_docs = text_splitter.split_documents(docs)
    print(f"   Split into {len(split_docs)} chunks")
    
    # Issue 6: Create vector store
    print("5. Creating vector store...")
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = FAISS.from_documents(split_docs, embedding_model)
    
    # Issue 7: Better retriever configuration
    print("6. Configuring retriever...")
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}  # Increased from 3
    )
    
    # Issue 8: Create improved prompt
    print("7. Creating improved prompt...")
    prompt = PromptTemplate(
        template=fixed_prompt_template, 
        input_variables=["context", "question"]
    )
    
    # Issue 9: Create the fixed RAG chain
    print("8. Creating fixed RAG chain...")
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])
    
    fixed_rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    print("✅ RAG Chain Fixed!")
    return fixed_rag_chain, vectordb

def test_fixed_rag():
    """Test the fixed RAG chain."""
    
    rag_chain, vectordb = fix_rag_chain()
    
    # Test questions
    test_questions = [
        "can you tell me how Reward Modeling works?",
        "What is LoRA?",
        "What are the main findings in the Llama 2 paper?"
    ]
    
    print("\n🧪 Testing Fixed RAG Chain...")
    print("=" * 60)
    
    for question in test_questions:
        print(f"\n❓ Question: {question}")
        print("-" * 40)
        
        try:
            # Get retrieved documents for debugging
            retriever = vectordb.as_retriever(search_kwargs={"k": 5})
            docs = retriever.get_relevant_documents(question)
            print(f"📄 Retrieved {len(docs)} documents")
            
            # Get answer
            answer = rag_chain.invoke(question)
            print(f"💡 Answer: {answer}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 40)

if __name__ == "__main__":
    test_fixed_rag() 