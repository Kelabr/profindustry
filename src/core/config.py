import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
DBNAME = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')

SECRET_KEY = 'hkgTYBFplhgyun859slkj'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
