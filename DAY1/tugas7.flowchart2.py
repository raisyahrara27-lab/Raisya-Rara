# Mulai program
print("=== PERHITUNGAN GAJI KARYAWAN ===")

# Input data karyawan
nama = input("Masukkan nama karyawan: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Hitung tunjangan, pajak, dan gaji bersih
tunjangan = 0.2 * gaji_pokok
total_pendapatan = gaji_pokok + tunjangan
pajak = 0.15 * total_pendapatan
gaji_bersih = total_pendapatan - pajak

# Output hasil perhitungan
print("\n--- HASIL PERHITUNGAN ---")
print(f"Nama Karyawan: {nama}")
print(f"Gaji Pokok: {gaji_pokok:.2f}")
print(f"Gaji Bersih: {gaji_bersih:.2f}")

# Selesai program