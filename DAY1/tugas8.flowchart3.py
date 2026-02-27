# Mulai program
print("=== PERHITUNGAN GAJI BERSIH KARYAWAN ===")

# Input nama dan gaji pokok
nama = input("Masukkan nama karyawan: ")
gaji_pokok = float(input("Masukkan jumlah gaji pokok: "))

# Proses perhitungan
tunjangan = 0.2 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

# Output hasil
print("\n=== HASIL PERHITUNGAN ===")
print(f"Nama: {nama}")
print(f"Gaji Pokok: Rp {gaji_pokok:.2f}")
print(f"Gaji Bersih: Rp {gaji_bersih:.2f}")

# Selesai program