import psycopg2

def connect():
    conn = psycopg2.connect("host=127.0.0.1 dbname=url-router user=postgres password=test port=5432")
    conn.set_session(autocommit=True)
    return conn