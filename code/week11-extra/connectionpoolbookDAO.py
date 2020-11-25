import mysql.connector
import dbconfig as cfg
class BookDAO:
    
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self): 
        db=self.initConnectToDB()
        db.close()
            
    def create(self, values):
        db = self.getConnection()
        cursor = db.cursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowId=cursor.lastrowid
        db.close()
        return lastRowId

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        db.close()
        return returnArray

    def findByID(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        book=self.convertToDictionary(result)
        db.close()
        return book

    def update(self, values):
        db = self.getConnection()
        cursor = db.cursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        db.close()

    def delete(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql="delete from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        db.close()
        

    def convertToDictionary(self, result):
        colnames=['id','Title','Author', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

bookDAO = BookDAO()