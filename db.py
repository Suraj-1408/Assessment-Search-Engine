import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DataBase Url not set properly in .env")
    
    return psycopg2.connect(DATABASE_URL)

