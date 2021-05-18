from abc import ABC, abstractmethod
from multipledispatch import dispatch

class Model (ABC):
    _table = ""
    _cnx = None

    _id = ""
    def __init__(self, cnx):
        self._cnx = cnx


    # overriding
    @dispatch(str)
    def execQ(self, query):
        try:
            self._cnx.getConnection().execute(query)
            return True
        except:
            return False
    
    @dispatch(str, tuple)
    def execQ(self, query, payload):
        try:
            self._cnx.getConnection().execute(query, payload)
            self._cnx.getDB().commit()
            return True
        except:
            return False
    

    @abstractmethod
    def create(self, payload):
        pass
    @abstractmethod
    def update(self, payload):
        pass
    @abstractmethod
    def getAll(self):
        pass
    @abstractmethod
    def delete(self, id):
        pass