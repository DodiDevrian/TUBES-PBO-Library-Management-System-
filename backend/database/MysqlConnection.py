from backend.database import Connection
import mysql.connector

class MysqlConnection(Connection.Connection):
    _ip = ""
    _port = ""
    _database = ""
    _user = ""
    _password = ""
    __db = ""
    __conn = ""
    def __init__(self, ip, port, database, user, password):
        self._ip = ip
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self.__db = mysql.connector.connect(
                        host=self._ip,
                        port=self._port,
                        user=self._user,
                        password=self._password,
                        database=self._database
                    )
        self.__conn = self.__db.cursor(buffered=True , dictionary=True)

    def getConnection(self):
        return self.__conn

    def getDB(self):
        return self.__db

    def setHost(self, ip, port):
        self._ip = ip
        self._port = port
    
    def getHostIp(self):
        return self._ip

    def getHostPort(self):
        return self._port
    
    def getDatabase(self):
        return self._database

    def setDatabase(self, database):
        self._database = database

    def setUser(self, user):
        self._user = user

    def setPassword(self, password):
        self._password = password

    def setDatabase(self, database):
        self._database = database