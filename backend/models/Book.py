from backend.models import Model
from multipledispatch import dispatch

class Book(Model.Model):
    def create(self, payload):
        query = "INSERT INTO books (name, created_at, updated_at) values (%s, now(), now())"
        if self.execQ(query, payload):
            print("======= DATA Buku CREATED =========")
        else:
            print("======= DATA Buku FAILED TO CREATE ==========")

    def update(self, payload):
        query = "UPDATE books set name=%s, updated_at = now() where id = %s"
        if self.execQ(query, payload):
            print("======= DATA Buku Updated =========")
        else:
            print("======= DATA Buku FAILED TO UPDATE ==========")

    @dispatch()
    def getAll(self):
        query = "SELECT * FROM books"
        if self.execQ(query):
            return self._cnx.getConnection().fetchall()
        else:
            print("Failed to GET ALL data Buku")
    
    def delete(self, id):
        query = "DELETE FROM books where id = %s"
        if self.execQ(query, (id,)):
            print("============= Buku berhasil dihapus ============")
        else:
            print("============= FAILED TO DELETE Buku ============")

    @dispatch(str)
    def getAll(self, searchValue):
        query = "SELECT * FROM books WHERE name LIKE %s"
        if self.execQ(query, (searchValue,)):
            return self._cnx.getConnection().fetchall()
        else:
            print("========= Failed to get data Buku =========")