**Endee Semantic Memory Search (RAG)**


**Project Overview**

This project demonstrates a simple Semantic Search / Mini-RAG memory system built using:

·	Endee Vector Database

·	Sentence Transformers

·	Python

The system converts text into vector embeddings and retrieves the most semantically similar memory based on a user query.

This simulates the retrieval component of Retrieval Augmented Generation (RAG).

**Problem Statement**

Traditional keyword search fails to understand meaning.

Vector databases enable semantic search, allowing retrieval based on meaning instead of exact words.

Example:

Query: "What is RAG?"

Retrieved Memory: "RAG combines retrieval and generation"

Even though the words differ, the meaning matches.

**How Endee is Used**

Endee is used as the vector storage layer for embeddings generated using SentenceTransformers.

In this prototype:

·	Endee runs locally using Docker

·	The Python application connects to Endee using the official Python SDK

·	The script automatically creates a vector index (if it does not exist)

·	Embeddings are stored and queried from Endee

This demonstrates how Endee can be integrated into a real RAG pipeline.

**System Architecture**

Pipeline:

1\.	User enters a query

2\.	SentenceTransformer converts text → 384-dim embedding

3\.	Embedding stored/retrieved from Endee vector DB

4\.	Most relevant memory returned


This represents the retrieval layer of a RAG system.



**Tech Stack**

·	Python

·	Endee Vector Database

·	SentenceTransformers

·	Docker

**Setup Instructions**

1\.	Run Endee using Docker

Install Docker, then run:

docker run -d -p 8080:8080 -v endee-data:/data --name endee-server endeeio/endee-server:latest


This starts the Endee vector database locally on port 8080.

2\. Install Python Dependencies

pip install -r requirements.txt

3\. Run the Project

python main.py

On first run, the script will automatically:

·	Connect to Endee

·	Create the memories vector index (if it does not exist)

·	Insert sample memories

·	Start the semantic search demo

·	No manual setup required.

**Example Queries**

Try asking:

What is RAG?

How do transformers work?

What are embeddings?

Why use vector databases?

**Future Improvements**

Store large document datasets in Endee
Integrate an LLM for full RAG pipeline
Build a web interface

***NOTE-***

***This project was developed using a fork of the official Endee repository, as required by the assignment.***





