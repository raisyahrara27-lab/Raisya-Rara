#Definisikan kelas Contact
class contact:
    def _init_(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email

    def tampilkan_(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Telepon: {self.nomor_telepon}")
        print(f"Email: {self.email}")
        print()

#Definisikan kelas Addressbook untuk mengelola daftar kontak
class AddressBook:
    def _init_(self):
        self.daftar_kontak = []

    def tambah_kontak (self, kontak):
        self.daftar_kontak.append(kontak)

    def tampilkan_semua_kontak(self):
        print("daftar kontak:")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()

# program utama
if _name_ == "_main_":
    address_book = Addressbook()

    while True:
        print("nama: ") 
        print("1, tambah kontak")            
        print("2, tampilkan semua kontak")
        print("3. keluar")

        pilihan = input("pilih menu (1/2/3): ")     

        if pilihan == "1":
            nama = input("nama: ")
            nomor_telepon = input("nomor telepon: ")
            email = input("email: ")
            kontak_baru = contact(nama, nomor_telepon, email)
            address_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            address_book.tampilkan_semua_kontak()
        elif pilihan == "3":
            break
        else:
            print("pilihan tidak valid. silakan pilih menu yang benar.")