 #Definisikan kelas dasar vehicle
class vehicle:
    def _init_(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

        def tampilkan_info(self):
            print(f"merk: {self.merk}")
            print(f"tahun: {self.tahun}")
            print(f"warna: {self.warna}")

#Definisikan kelas trunan car yang mewarisi dari vehicle
class car(vehicle):
    def _init_(self, merk, tahun, warn, model):
            # Panggil konstruktor kelas dasar
            super()._init_(merk, tahun, warna)
            self.model = ModuleNotFoundError

    def tampilkan_info(self):
            # panggil metode kelas dasar untuk menampilkan info kendaraan
            super().tampilkan_info()
            print(f"model: {self.mode}")

# program utama
if _name_== "_main_":
     car = car("Toyota", 2022, "Merah", "Camry")

     print("info kendaran:")
     car.tampilkan_info()