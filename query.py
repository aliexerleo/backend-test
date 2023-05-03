import psycopg2
from psycopg2 import Error
from connection import create_connection

def list_all_users():
    conn = create_connection()
    sql = 'SELECT * FROM public.users'

    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            column_names = tuple(str(column[0], "utf-8")
                                    if isinstance(column[0], bytes) else column[0]
                                    for column in cur.description)

            for row in cur:
                yield dict(zip(column_names, row))
    except Error as e:
        print(f'Error at list_all_users(): {str(e)}')
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def add_users(data):
    conn = create_connection()
    sql = "INSERT INTO public.users (id, Full_name, birth, email) VALUES (%s, %s, %s, %s)";
    try:
        with conn.cursor() as cur:
            cur.execute(sql, data)
            conn.commit()
    except Error as e:
        print(f'Error at list_all_users(): {str(e)}')
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


