from backend.models import User
def login(cnx, username, password):
    
    user = User.User(cnx)
    auth = user.get(username, password)
    if auth:
        return {
            "id" : auth['id'],
            "username": auth['username'],
        }
    else:
        print("Username or password is wrong!")
        return False
