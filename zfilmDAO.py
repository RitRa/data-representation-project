import pymysql

import config as cfg
# data access object
class FilmDAO:
    db=""

    def connectToBD(self):
        self.db = pymysql.connect(
            host=cfg.pymysql['host'],
            user=cfg.pymysql['user'],
            password=cfg.pymysql['password'],
            database=cfg.pymysql['database']
        )

    def __init__(self):
        self.connectToBD()

    def getCursor(self):
        if self.db.open:
            self.connectToBD()
        return self.db.cursor()


    def create(self, values):
        cursor = self.getCursor()
        sql="insert into film (title, director, year) values (%s,%s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowId = cursor.lastRowId
        cursor.close()
        return lastRowId

    def getAll(self):
        cursor = self.getCursor()
        sql="select * from film"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from film where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.getCursor()
        sql="update film set title= %s, director=%s, year=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        print("UPDATED")

    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from film where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
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


    def checkUser(self, email, password):
        cursor = self.getCursor()
        sql="SELECT * FROM usertable where email = %s and password=%s"
        values = (email, password)
        cursor.execute(sql, values)
            # Fetch one record and return result
        account = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary2(account)

            #result = cursor.fetchone()
            #ßprint(result)
        print("Hello Rita")

    def convertToDictionary2(self, account):
        colnames=["id", "name", "email", "password"]
        print(colnames)
        item = {}

        if account:
            for i, colname in enumerate(colnames):
                print(colnames)
                value = account[i]
                item[colname] = value
        return item

filmDAO = FilmDAO()