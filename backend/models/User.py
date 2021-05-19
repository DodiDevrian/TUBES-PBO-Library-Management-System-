from backend.models import Model
from multipledispatch import dispatch

class User(Model.Model):
    def create(self, payload):
        query = "INSERT INTO users (username, password, created_at, updated_at) values (%s, %s, now(), now())"
        if self.execQ(query, payload):
            print("======= DATA ADMIN CREATED =========")
        else:
            print("======= DATA ADMIN FAILED TO CREATE ==========")

    def update(self, payload):
        query = "UPDATE users set username=%s, password=%s, updated_at = now() where id = %s"
        if self.execQ(query, payload):
            print("======= DATA ADMIN Updated =========")
        else:
            print("======= DATA ADMIN FAILED TO UPDATE ==========")

    @dispatch()
    def getAll(self):
        query = "SELECT * FROM users"
        if self.execQ(query):
            return self._cnx.getConnection().fetchall()
        else:
            print("Failed to GET ALL data admin")
    
    def delete(self, id):
        query = "DELETE FROM users where id = %s"
        if self.execQ(query, (id,)):
            print("============= ADMIN berhasil dihapus ============")
        else:
            print("============= FAILED TO DELETE ADMIN ============")

    @dispatch(str)
    def getAll(self, searchValue):
        query = "SELECT * FROM users WHERE username LIKE %s"
        if self.execQ(query, (searchValue,)):
            return self._cnx.getConnection().fetchall()
        else:
            print("========= Failed to get data admin =========")

    @dispatch(str)
    def get(self, id):
        query = "SELECT * FROM users where id=%s"
        if self.execQ(query, (id,)):
            return self._cnx.getConnection().fetch()
        else:
            return False
    
    @dispatch(str, str)
    def get(self, username, password):
        query="SELECT * FROM users where username=%s and password=%s"
        if self.execQ(query, (username, password,)):
            data = self._cnx.getConnection().fetchall()
            if len(data) < 1:
                return False
            return data[0]
        else:
            return False
