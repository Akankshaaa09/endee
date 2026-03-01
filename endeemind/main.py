from endee import Endee
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

client = Endee()

INDEX_NAME = "memories"
DIMENSION = 384

# Create index
try:
    print("Ensuring Endee index exists...")
    client.create_index(
        name=INDEX_NAME,
        dimension=DIMENSION,
        space_type="cosine",
        precision="float16"
    )
except Exception as e:
    print("Index already exists. Continuing...")

index = client.get_index(name=INDEX_NAME)

def embed(text):
    return model.encode(text).tolist()

def store(text, id):
    vector = embed(text)

    index.upsert([
        {
            "id": id,
            "vector": vector,
            "meta": {"text": text}
        }
    ])

    print("Stored:", text)

def search(query):
    vector = embed(query)

    results = index.query(
        vector=vector,
        top_k=3
    )

    print("\nTop Matches:")
    for item in results:
        print("-", item["meta"]["text"], "| score:", round(item["similarity"], 4))


# Demo data
memories = [
    "Transformers use attention",
    "Vector databases store embeddings",
    "Embeddings convert text to vectors",
    "RAG combines retrieval and generation",
]

for i, m in enumerate(memories):
    store(m, f"id{i}")

while True:
    q = input("\nAsk something (type exit to quit): ")
    if q == "exit":
        break
    search(q)