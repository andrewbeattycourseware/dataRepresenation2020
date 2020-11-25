from connectionpoolbookDAO import bookDAO as bookDAO

books = bookDAO.getAll()
for book in books:
    print (book)