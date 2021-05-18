from backend.models import Model
from multipledispatch import dispatch

class Peminjaman(Model.Model):
    def create(self, payload):
        query = "INSERT INTO peminjaman (book_id, member_id, days, denda, created_at, updated_at) values (%s, %s, %s, %s, now(), now())"
        if self.execQ(query, payload):
            print("======= DATA PEMINJAMAN CREATED =========")
        else:
            print("======= DATA PEMINJAMAN FAILED TO CREATE ==========")

    def update(self, payload):
        query = "UPDATE peminjaman set returned_at= now(), updated_at = now() where id = %s"
        if self.execQ(query, payload):
            print("======= DATA PEMINJAMAN Updated =========")
        else:
            print("======= DATA PEMINJAMAN FAILED TO UPDATE ==========")

    @dispatch()
    def getAll(self):
        query = "SELECT * FROM peminjaman where returned_at is null"
        if self.execQ(query):
            return self._cnx.getConnection().fetchall()
        else:
            print("Failed to GET ALL data PEMINJAMAN")
    
    def delete(self, id):
        query = "DELETE FROM peminjaman where id = %s"
        if self.execQ(query, (id,)):
            print("============= PEMINJAMAN berhasil dihapus ============")
        else:
            print("============= FAILED TO DELETE PEMINJAMAN ============")

    @dispatch(str)
    def getAll(self, searchValue):
        query = "SELECT * FROM peminjaman WHERE name LIKE %s"
        if self.execQ(query, (searchValue,)):
            return self._cnx.getConnection().fetchall()
        else:
            print("========= Failed to get data PEMINJAMAN =========")

    def get(self, id):
        query="SELECT * FROM peminjaman where id=%s"
        if self.execQ(query, (id,)):
            data = self._cnx.getConnection().fetchall()
            if len(data) < 1:
                return False
            return data[0]
        else:
            return False