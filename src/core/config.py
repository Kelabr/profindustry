import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DBNAME = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')
