import psycopg2
import faiss
import json
from sentence_transformers import SentenceTransformer
import numpy as np
from db import get_connection

conn = get_connection()
cursor = conn.cursor()


# Fetch assessments
cursor.execute("SELECT id, name, description FROM assessments;")
rows = cursor.fetchall()

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Prepare lists
texts = []
metadata = []

for row in rows:
    id_, name, desc = row
    full_text = f"{name} - {desc}"
    texts.append(full_text)
    metadata.append({"id": id_, "name": name})

# Generate embeddings
embeddings = model.encode(texts, convert_to_numpy=True)

# Store in FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "faiss_index.index")

# Save metadata
with open("assessments.json", "w") as f:
    json.dump(metadata, f)

print("FAISS index and metadata saved successfully.")

# Cleanup
cursor.close()
conn.close()
