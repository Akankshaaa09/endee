print("SCRIPT STARTED")

import requests
import uuid
from sentence_transformers import SentenceTransformer

BASE = "http://localhost:8080/api/v1/index/memories"

print("Loading AI embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text):
    return model.encode(text).tolist()


# STORE MEMORY
def store_memory():
    text = input("\nEnter note: ")

    payload = {
        "vectors": [
            {
                "id": str(uuid.uuid4()),
                "vector": embed(text),   # ✅ CORRECT FIELD
                "metadata": {"text": text}
            }
        ]
    }

    try:
        r = requests.post(f"{BASE}/insert", json=payload)

        if r.status_code == 200:
            print("✅ Stored successfully")
        else:
            print("❌ Error:", r.status_code, r.text)

    except Exception as e:
        print("❌ Connection error:", e)


# SEARCH MEMORY
def search_memory():
    query = input("\nEnter search query: ")

    payload = {
        "vector": embed(query),   # ✅ CORRECT FIELD
        "k": 3
    }

    try:
        r = requests.post(f"{BASE}/search", json=payload)

        if r.status_code == 200:
            print("\nResults:")
            print(r.text)
        else:
            print("❌ Error:", r.status_code, r.text)

    except Exception as e:
        print("❌ Connection error:", e)


# MENU LOOP
while True:

    print("\n====== AI MEMORY SYSTEM ======")
    print("1. Store memory")
    print("2. Search memory")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        store_memory()

    elif choice == "2":
        search_memory()

    elif choice == "3":
        break

    else:
        print("Invalid choice")