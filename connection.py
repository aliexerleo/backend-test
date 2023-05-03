import psycopg2
from psycopg2 import Error

def create_connection():
    conn = None

    try:
        conn = psycopg2.connect(
                host='localhost',
                database='new_school',
                user='myschool',
                password='School2020'
        )
    except Error as e:
        print('Error at create_connection()' + str(e))
    return conn
