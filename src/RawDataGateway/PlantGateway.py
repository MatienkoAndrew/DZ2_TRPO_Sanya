import psycopg2
from contextlib import closing


class PlantGateway:
    def __init__(self):
        self.plant = None
        self.length = None
        self.weight = None

        self.tablename = 'plants'
        self.connect = "host='localhost' dbname='postgres' user='a19053183' password=''"

    def Insert(self):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO {self.tablename} (name, length, weight)
                            VALUES ('{self.plant}', '{self.length}', {self.weight})
                            """)
                conn.commit()
        return

    def getAll(self):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""
                    SELECT * FROM {self.tablename}
                """)

                rows = cursor.fetchall()
        return rows

    def getLastId(self):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT id FROM {self.tablename}""")
                lastId = cursor.fetchall()[-1][0]
        return lastId

    def getLastPlant(self, id):
        with closing(psycopg2.connect(self.connect)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM {self.tablename} WHERE id = {id}""")
                plantInfo = cursor.fetchone()
        return plantInfo
