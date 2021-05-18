from backend.models import Peminjaman
from datetime import datetime

def create(cnx, bukuID, anggotaID, days, denda):
    peminjaman = Peminjaman.Peminjaman(cnx)
    peminjaman.create((bukuID, anggotaID, days, denda,))

def pengembalian(cnx, id):
    peminjaman = Peminjaman.Peminjaman(cnx)
    data = peminjaman.get(id)
    if data == False:
        print("NOT FOUND")
        return False
    div = datetime.now() - data['created_at'] 
    if div.days > data['days']:
        margin = div.days - data['days']
        denda = margin * data['denda']
        print("TELAT "+str(margin)+" HARI")
        print("DENDA YANG HARUS DIBAYAR: ")
        print("Rp. "+ str(denda))
    else:
        print("Tidak ada denda!")
    peminjaman.update((id,))
    print("BERHASIL DI KEMBALIKAN")

def getAll(cnx):
    peminjaman = Peminjaman.Peminjaman(cnx)
    return peminjaman.getAll()

def delete(cnx, id):
    peminjaman = Peminjaman.Peminjaman(cnx)
    peminjaman.delete(id)

def search(cnx, searchValue):
    peminjaman = Peminjaman.Peminjaman(cnx)
    return peminjaman.getAll("%"+searchValue+"%")