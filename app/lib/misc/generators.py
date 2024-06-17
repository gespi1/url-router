import uuid
from lib.db.pg_client import connect

def generateUniqueID():
    conn = connect()
    try:
        cur = conn.cursor()
        id = uuid.uuid4()
        cur.execute(f"SELECT EXISTS(SELECT 1 FROM public.routes WHERE id='{id}');")
        result = bool(cur.fetchone()[0])
        while result:
            id = uuid.uuid4()
            cur.execute(f"SELECT EXISTS(SELECT 1 FROM public.routes WHERE id='{id}');")
            result = bool(cur.fetchone()[0])
        return str(id)
    finally:
        cur.close()
        conn.close()