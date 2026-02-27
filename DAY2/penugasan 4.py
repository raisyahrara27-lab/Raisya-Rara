import math

# definisikan kelas dasar shape
class shape:
    def hitung_luas(self):
        pass

# definisikan kelas turunan square yang mewarisi dari shape
    class square(shape):
        def _init_(self, sisi):
            self.sisi = sisi 

        def hitung_luas(self):
            return self.sisi ** 2
        
# definisikan kelas turunan circle yang mewarisi dari shape
    class circle(shape):
        def _init_(self, radius):
                self.radius = radius

        def jitung_luas(self):
                return math.pi * self.radius ** 2
            
# definisikan kelas turunan triangle yang mewarisi dari shape
    class triangle(shape):
        def _init_(self, alas, tinggi):
            self.alas = alas
            self.tinggi = tinggi

        def hitung_luas(self):
             return 0.5 * self.alas * self.tinggi

# program utama

                    