import pymysql.cursors

import config as cfg
# data access object

class UserDAO:
    db=""

    def __init__(self):
        self.db = pymysql.connect(
        host=cfg.pymysql['host'],
        user=cfg.pymysql['user'],
        password=cfg.pymysql['password'],
        database=cfg.pymysql['database']
        )


    
    def checkUser(self, email, password):
        cursor = self.db.cursor()
        sql="SELECT * FROM usertable where email = %s and password=%s"
        values = (email, password)
        cursor.execute(sql, values)
        # Fetch one record and return result
        account = cursor.fetchone()
        return self.convertToDictionary(account)
       
        #result = cursor.fetchone()
        #ßprint(result)
        print("Hello Rita")
    
    def convertToDictionary(self, account):
        colnames=["id", "name", "email", "password"]
        print(colnames)
        item = {}
        
        if account:
            for i, colname in enumerate(colnames):
                print(colnames)
                value = account[i]
                item[colname] = value
        return item    
        
        


userDAO = UserDAO()