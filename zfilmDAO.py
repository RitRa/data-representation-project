import pymysql.cursors

import config as cfg
# data access object
class FilmDAO:
    db=""

    def __init__(self):
        self.db = pymysql.connect(
        host=cfg.pymysql['host'],
        user=cfg.pymysql['user'],
        password=cfg.pymysql['password'],
        #user="datarep", # this is the user name on my mac
        #passwd="password" # for my mac
        database=cfg.pymysql['database']
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into film (title, director, year) values (%s,%s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid
            
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from film"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from film where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update film set title= %s, director=%s, year=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        print("UPDATED")

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from film where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
    
    def convertToDictionary(self, result):
        colnames=["id", "title", "director", "year"]
        print(colnames)
        item = {}
        
        if result:
            for i, colname in enumerate(colnames):
                print(colnames)
                value = result[i]
                item[colname] = value
        return item

filmDAO = FilmDAO()
