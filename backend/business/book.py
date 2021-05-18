from backend.models import Book

def create(cnx, name):
    book = Book.Book(cnx)
    book.create((name,))

def update(cnx, id, name):
    book = Book.Book(cnx)
    book.update((name, id,))

def getAll(cnx):
    book = Book.Book(cnx)
    return book.getAll()

def delete(cnx, id):
    book = Book.Book(cnx)
    book.delete(id)

def search(cnx, searchValue):
    book = Book.Book(cnx)
    return book.getAll("%"+searchValue+"%")