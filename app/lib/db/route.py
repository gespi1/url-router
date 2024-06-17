import lib.db.pg_client as pg_client
class Route:
    def __init__(self, id):
        self.id = id
        self.pg_conn = pg_client.connect()
        self.exist = self.idExist()

    def idExist(self):
        result = self.exeQuery(f"SELECT EXISTS(SELECT 1 FROM public.routes WHERE id='{self.id}');")
        return bool(result[0]) # returns tuple, extract boolean result

    def getLink(self):
        result = self.exeQuery(f"SELECT linkto FROM public.routes WHERE id='{self.id}';")
        return result[0]
    
    def exeQuery(self, query):
        cur = self.pg_conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        return result
    
    def closeDBconn(self):
        self.pg_conn.close()
        
    # def test(self):
    #     result = self.exeQuery(f"SELECT * FROM public.routes;")
    #     print(result)