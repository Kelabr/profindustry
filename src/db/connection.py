import psycopg2
from psycopg2 import OperationalError
from ..core.config import HOST, DBNAME, USER, PASSWORD, PORT

def connection():
    try:
        coon = psycopg2.connect(
            host=HOST,
            dbname=DBNAME,
            user=USER,
            password=PASSWORD,
            port=PORT
        )

        return coon
    
    except OperationalError as e:
        print('Error in Connection', e)
        return None