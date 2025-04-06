#if __name__ == "__main__":
import psycopg2
import faiss
import json
from sentence_transformers import SentenceTransformer
import numpy as np
#from tabulate import tabulate 
from db import get_connection


# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index
index = faiss.read_index("faiss_index.index")

# Load metadata
with open("assessments.json", "r") as f:
    metadata = json.load(f)


conn = get_connection()
cur = conn.cursor()



#defining  a function that searches for specific assessments. if found return assessment ids.
def search_assessments(usr_query):
    query_vector = model.encode([usr_query])
    D,I = index.search(np.array(query_vector),k=3)
    top_ids = [metadata[idx]["id"] for idx in I[0]]

    return top_ids


#function to get the details of function if found.
def get_assessements_details(top_ids):
    placeholders = ','.join(['%s'] * len(top_ids))
    query = f"""
    select id,name,url,remote_testing_support,duration,test_type,adaptive_support from assessments where id in ({placeholders})
    """

    cur.execute(query,top_ids)
    
    return cur.fetchall()

