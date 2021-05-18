from frontend import menu
from backend.database import MysqlConnection
def main(cnx):
    print("Selamat datang di perpustakaan xyz")
    menu.main_menu(cnx)
    main(cnx)
    

if __name__=="__main__":
    mysql = MysqlConnection.MysqlConnection("localhost", "3306", "perpus" , "root", "")
    main(mysql)
