import getpass
from backend.business import auth
from frontend import menu

def insertUsernamePassword(cnx):
    print("====== LOGIN ======")
    username = input("username: ")
    password = getpass.getpass("Password: ")

    dataAuth = auth.login(cnx, username, password)
    if dataAuth:
        menu.menu_admin(cnx, dataAuth)
    else:
        menu.auth_failed(cnx)
