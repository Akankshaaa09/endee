import requests
from sentence_transformers import SentenceTransformer

BASE = "http://localhost:8080/api/v1/index/memories"

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text):
    return model.encode(text).tolist()


def store(text, id):
    payload = {
        "vectors": [
            {
                "id": id,
                "vector": embed(text),   # ← THIS IS THE FIX
                "metadata": {"text": text}
            }
        ]
    }

    r = requests.post(f"{BASE}/insert", json=payload)

    print("\nStored:", text)
    print("Status:", r.status_code)
    print(r.text)


def search(query):
    payload = {
        "query_vector": embed(query),   # ← THIS IS THE FIX
        "k": 3
    }

    r = requests.post(f"{BASE}/search", json=payload)

    print("\nResults:")
    print(r.text)


memories = [
    "Transformers use attention",
    "Vector databases store embeddings",
    "Embeddings convert text to vectors",
    "RAG combines retrieval and generation",
]

for i, m in enumerate(memories):
    store(m, f"id{i}")


while True:
    q = input("\nAsk something (or exit): ")

    if q == "exit":
        break

    search(q)