#Muhammad Restu Al-Hidayat
#2309116067
print("-----------------------------------")
print("Hi, Gens")
print("Selamat datang di Genservice")
print("-----------------------------------")

from prettytable import PrettyTable

# list untuk menyimpan data
data_service= [
    ["001", "Install Ulang", 150000],
    ["002", "Perbaikan IC", 750000],
    ["003", "Ganti LCD", 900000],
    ["004", "Ganti Keyboard", 400000],
    ["005", "Service Engsel", 500000], 

]

# pembeli
def transaksi():
    while True:
        # menampilkan daftar service
        print("Daftar service yang Tersedia")
        show_item()
        
        id_item = input("Masukkan Kategori Service: ")
        qty = int(input("Jumlah : "))
        
        # memeriksa apakah jumlah perbaikan sesuai
        for item in data_service:
            if item[0] == id_item:
                if qty > 1:
                    print("Maaf, jumlah maksimum perbaikan adalah 1!")
                    break
        else:
            # menampilkan total harga
            for i in range(len(data_service)):
                if data_service[i][0] == id_item:
                    total_harga = data_service[i][2] * qty
                    print("Total harga: Rp", total_harga)
                    return
        
        # menampilkan kembali tampilan daftar item apabila input salah
        print()

# admin
def create():
    # input data item yang baru
    id_item = input("Masukkan ID item: ")
    nama_item = input("Masukkan nama item: ")
    harga_item = int(input("Masukkan harga item: "))
    
    # menambahkan item yang baru ke dalam database
    data_service.append([id_item, nama_item, harga_item])
    
    # menampilkan daftar item lengkap dengan item baru yang ditambahkan
    show_item()

def read():
    # menampilkan seluruh item yang terdapat dalam database
    show_item()

def update():
    # input id item yang ingin diperbarui
    id_item = input("Masukkan ID item yang ingin di-update data: ")
    for i in range(len(data_service)):
        if data_service[i][0] == id_item:
            # input data item yang baru
            nama_item = input("Masukkan nama item baru: ")
            harga_item = int(input("Masukkan harga item baru: "))
            
            # melakukan update item yang dipilih
            data_service[i][1] = nama_item
            data_service[i][2] = harga_item
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Item tidak ditemukan")

def delete():
    # input id item yang ingin dihapus
    id_item = input("Masukkan ID item yang ingin dihapus: ")
    for i in range(len(data_service)):
        if data_service[i][0] == id_item:
            # menghapus item sesuai input id
            data_service.pop(i)
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Item tidak ditemukan")
    
# menampilkan seluruh item yang terdapat dalam database dengan prettytable
def show_item():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Item", "Harga"]
    for item in data_service:
        table.add_row(item)
    print(table)

# program utama
while True:
    print("="*30)
    print("GENSERVICE")
    print("="*30)
    print("1. Admin")
    print("2. Pembeli")
    print("3. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        print("="*30)
        print("ADMIN GENSERVICE")
        print("="*30)
        print("1. Tambah Item")
        print("2. Lihat Item")
        print("3. Update Item")
        print("4. Hapus Item")
        print("5. Kembali")

        admin_choice = input("Pilih menu: ")
        if admin_choice == "1":
            create()
        elif admin_choice == "2":
            read()
        elif admin_choice == "3":
            update()
        elif admin_choice == "4":
            delete()
        elif admin_choice == "5":
            continue
        else:
            print("Menu tidak tersedia")

    elif choice == "2":
        print("="*30)
        print("PEMBELI")
        print("="*30)
        transaksi()
    elif choice == "3":
        print("Aplikasi Selesai Berjalan")
        break
    else:
        print("Menu tidak tersedia")
