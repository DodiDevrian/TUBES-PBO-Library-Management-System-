from backend.models import Member
def create(cnx, name):
    member = Member.Member(cnx)
    member.create((name,))

def update(cnx, id, name):
    member = Member.Member(cnx)
    member.update((name, id,))

def getAll(cnx):
    member = Member.Member(cnx)
    return member.getAll()

def delete(cnx, id):
    member = Member.Member(cnx)
    member.delete(id)

def search(cnx, searchValue):
    member = Member.Member(cnx)
    return member.getAll("%"+searchValue+"%")