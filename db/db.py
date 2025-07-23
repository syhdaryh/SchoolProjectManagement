import os
import psycopg2

def get_connection():
    return psycopg2.connect(os.getenv("DB_URL"))
