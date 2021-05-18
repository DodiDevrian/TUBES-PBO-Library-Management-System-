from frontend import menu
from backend.database import MysqlConnection
def main(cnx):
    print("Selamat datang di perpustakaan xyz")
    menu.main_menu(cnx)
    main(cnx)
    

if __name__=="__main__":
    mysql = MysqlConnection.MysqlConnection("127.0.0.1", "33061", "perpus" , "root", "131028")
    main(mysql)