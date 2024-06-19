import lib.db.pg_client as pg_client

class Route:
    def __init__(self, id):
        self.id = id
        self.pg_conn = pg_client.connect()
        self.exist = self.idExist()
        self.link = ""

    def idExist(self):
        cur = self.pg_conn.cursor()
        cur.execute(f"SELECT EXISTS(SELECT 1 FROM public.routes WHERE id='{self.id}');")
        result = cur.fetchone()[0] # returns tuple, extract boolean result
        cur.close()
        return bool(result) 

    def setLink(self, link):
        self.link = link

    def getLink(self):
        cur = self.pg_conn.cursor()
        cur.execute(f"SELECT linkto FROM public.routes WHERE id='{self.id}';")
        self.link  = cur.fetchone()[0]
        cur.close()
        return self.link

    def createRoute(self):
        cur = self.pg_conn.cursor()
        cur.execute(f"INSERT INTO public.routes (id, linkto) VALUES ('{self.id}', '{self.link}');")
        cur.close()
        
    def closeDBconn(self):
        self.pg_conn.close()
