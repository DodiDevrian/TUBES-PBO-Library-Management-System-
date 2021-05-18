from backend.models import Model
from multipledispatch import dispatch

class Member(Model.Model):
    def create(self, payload):
        query = "INSERT INTO members (name, created_at, updated_at) values (%s, now(), now())"
        if self.execQ(query, payload):
            print("======= DATA MEMBER CREATED =========")
        else:
            print("======= DATA MEMBER FAILED TO CREATE ==========")

    def update(self, payload):
        query = "UPDATE members set name=%s, updated_at = now() where id = %s"
        if self.execQ(query, payload):
            print("======= DATA MEMBER Updated =========")
        else:
            print("======= DATA MEMBER FAILED TO UPDATE ==========")

    @dispatch()
    def getAll(self):
        query = "SELECT * FROM members"
        if self.execQ(query):
            return self._cnx.getConnection().fetchall()
        else:
            print("Failed to GET ALL data MEMBER")
    
    def delete(self, id):
        query = "DELETE FROM members where id = %s"
        if self.execQ(query, (id,)):
            print("============= MEMBER berhasil dihapus ============")
        else:
            print("============= FAILED TO DELETE MEMBER ============")

    @dispatch(str)
    def getAll(self, searchValue):
        query = "SELECT * FROM members WHERE name LIKE %s"
        if self.execQ(query, (searchValue,)):
            return self._cnx.getConnection().fetchall()
        else:
            print("========= Failed to get data MEMBER =========")