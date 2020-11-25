import mysql.connector
import dbconfig as cfg
class BookDAO:
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database']
        )
    def __init__(self): 
        self.connectToDB()
     
    
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()
    
            
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowId=cursor.lastrowid
        cursor.close()
        return lastRowId

    def getAll(self):
        cursor = self.getCursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray

    def findByID(self, id):
        cursor = self.getCursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        book=self.convertToDictionary(result)
        cursor.close()
        return book

    def update(self, values):
        cursor = self.getCursor()
        sql="update book set title= %s,author=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        cursor.close()
        

    def convertToDictionary(self, result):
        colnames=['id','Title','Author', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
bookDAO = BookDAO()