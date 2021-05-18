from backend.models import User
def create(cnx, username, password):
    user = User.User(cnx)
    user.create((username, password,))

def update(cnx, id, username, password):
    user = User.User(cnx)
    user.update((username, password, id,))

def getAll(cnx):
    user = User.User(cnx)
    return user.getAll()

def delete(cnx, id):
    user = User.User(cnx)
    user.delete(id)

def search(cnx, searchValue):
    user = User.User(cnx)
    return user.getAll("%"+searchValue+"%")