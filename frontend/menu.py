from frontend import login
from backend.business import admin
from backend.business import member
from backend.business import book
from backend.business import peminjaman

import getpass

def main_menu(cnx):
    login.insertUsernamePassword(cnx)
    
def auth_failed(cnx):
    print("1. Try Again")
    print("2. Exit")
    pil = input("Pilihan: ")
    if pil=="1":
        login.insertUsernamePassword(cnx)
    elif pil == "2":
        return

def menu_admin(cnx, dataAuth):
    print("1. List Admin (Tambah, Hapus, Ubah, Cari)")
    print("2. List Anggota (Tambah, Hapus, Ubah, Cari)")
    print("3. List Buku (Tambah, Hapus, Ubah, Cari)")
    print("4. Peminjaman")
    print("5. Pengembalian")
    print("6. Logout")
    pil = input("Pilihan: ")
    if pil == "6":
        print("")
        print("======== BERHASIL LOGOUT ========")
        login.insertUsernamePassword(cnx)
        return
    elif pil=="1":
        menu_admin_admin(cnx)
    elif pil=="2":
        menu_admin_anggota(cnx)
    elif pil=="3":
        menu_admin_buku(cnx)
    elif pil=="4":
        menu_admin_peminjaman(cnx)
    elif pil=="5":
        menu_admin_pengembalian(cnx)
    menu_admin(cnx, dataAuth)

def menu_admin_admin(cnx):
    datas = admin.getAll(cnx)
    print("======== LIST Admin ========")
    print("----------------------------------------------------")
    print("ID\t\tusername")
    print("----------------------------------------------------")
    for v in datas:
        print(str(v['id']) + "\t\t" + v['username'])
    print("----------------------------------------------------")
    print("1. Tambah")
    print("2. Edit")
    print("3. Hapus")
    print("4. Cari")
    print("5. Back")
    pil = input("Pilihan: ")
    if pil == "1":
        print("======= TAMBAH ADMIN BARU =======")
        username = input("username: ")
        password = getpass.getpass("password: ")
        admin.create(cnx, username, password)

    elif pil == "2":
        adminID = input("Masukkan id admin: ")
        username = input("username: ")
        password = getpass.getpass("password: ")
        admin.update(cnx, adminID, username, password)
    elif pil == "3":
        adminID = input("Masukkan id admin: ")
        admin.delete(cnx, adminID)
    elif pil == "4":
        searchValue = input("Masukkan keyword: ")
        users = admin.search(cnx, searchValue)
        print("=========== SEARCH DATA ADMIN =================")
        print("----------------------------------------------------")
        print("ID\t\tusername")
        print("----------------------------------------------------")
        for v in users:
            print(str(v['id']) + "\t\t" + v['username'])
        print("===============================================")
    elif pil == "5":
        return
    else:
        print("PILIHAN TIDAK TERSEDIA")
        menu_admin_admin(cnx)

def menu_admin_anggota(cnx):
    datas = member.getAll(cnx)
    print("======== LIST anggota ========")
    print("ID\t\tName")
    for v in datas:
        print(str(v['id']) + "\t\t" + v['name'])
   
    print("")
    print("1. Tambah")
    print("2. Edit")
    print("3. Hapus")
    print("4. Cari")
    print("5. Back")
    pil = input("Pilihan: ")
    if pil == "1":
        print("======= TAMBAH ANGGOTA BARU =======")
        name = input("Masukkan nama anggota: ")
        member.create(cnx, name)
    elif pil == "2":
        memberID = input("Masukkan id anggota: ")
        name = input("Masukkan nama: ")
        member.update(cnx, memberID, name)
    elif pil == "3":
        memberID = input("Masukkan id anggota: ")
        member.delete(cnx, memberID)
    elif pil == "4":
        searchValue = input("Masukkan keyword: ")
        members = member.search(cnx, searchValue)
        print("=========== SEARCH DATA MEMBER =================")
        print("----------------------------------------------------")
        print("ID\t\tName")
        print("----------------------------------------------------")
        for v in members:
            print(str(v['id']) + "\t\t" + v['name'])
        print("===============================================")
    elif pil == "5":
        return
    else:
        print("PILIHAN TIDAK TERSEDIA")
        menu_admin_anggota(cnx)

def menu_admin_buku(cnx):
    datas = book.getAll(cnx)
    print("======== LIST buku ========")
    for v in datas:
            print(str(v['id']) + "\t\t" + v['name'])
    print("")
    print("1. Tambah")
    print("2. Edit")
    print("3. Hapus")
    print("4. Cari")
    print("5. Back")
    pil = input("Pilihan: ")
    if pil == "1":
        print("======= TAMBAH BUKU BARU =======")
        name = input("Masukkan nama Buku: ")
        book.create(cnx, name)

    elif pil == "2":
        bookID = input("Masukkan id Buku: ")
        name = input("Masukkan nama: ")
        book.update(cnx, bookID, name)
    elif pil == "3":
        bookID = input("Masukkan id buku: ")
        book.delete(cnx, bookID)
    elif pil == "4":
        searchValue = input("Masukkan keyword: ")
        datas = book.search(cnx, searchValue)
        print("======== LIST buku ========")
        for v in datas:
            print(str(v['id']) + "\t\t" + v['name'])

    elif pil == "5":
        return
    else:
        print("PILIHAN TIDAK TERSEDIA")
        menu_admin_anggota(cnx)

def menu_admin_peminjaman(cnx):
    bukuID = input("Masukkan id buku: ")
    anggotaID = input("Masukkan id anggota: ")
    days = input("Berapa lama ? (hari): ")
    denda = input("denda: Rp.")
    peminjaman.create(cnx, bukuID, anggotaID, days, denda)


def menu_admin_pengembalian(cnx):
    datas = peminjaman.getAll(cnx)
    print("===== LIST PEMINJAMAN ======")
    print("ID\t\tMember ID\t\tBook ID")
    for v in datas:
            print(str(v['id']) + "\t\t" + str(v['member_id']) + "\t\t\t" + str(v['book_id']))
    peminjamanID = input("Masukkan ID peminjaman: ")
    data = peminjaman.pengembalian(cnx, peminjamanID)
   
