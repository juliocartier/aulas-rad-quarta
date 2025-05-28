from dotenv import load_dotenv
import os

load_dotenv()

import pg8000

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def conexao_banco():
    conn = pg8000.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, port=5432, database=DB_NAME)
    return conn
