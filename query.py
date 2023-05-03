import psycopg2
from psycopg2 import Error
from connection import create_connection

def list_all_users():
    conn = create_connection()
    sql = 'SELECT * FROM public.users'

    try:
        cur = conn.cursor()
        cur.execute(sql)
        query = cur.fetchall()
        return query
    except Error as e:
        print(f'Error at list_all_users(): {str(e)}')
        return false
    finally:
        if conn:
            cur.close()
            conn.close()