import psycopg2
from psycopg2 import Error

def create_connection():
    conn = None

    try:
        conn = psycopg2.connect(
                host='localhost',
                database='postgres',
                user='postgres',
                password='postgres'
        )
    except Error as e:
        print('Error at create_connection()' + str(e))
    return conn
