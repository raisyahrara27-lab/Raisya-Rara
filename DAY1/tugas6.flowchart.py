#inisialisasi variabel untuk memulai perulangan
ulang = "ya"

while ulang == "ya":
    #1. input nilai siswa 
    nilai_siswa = float(input("Masukkan nilai siswa: "))

    #. cek apakah nilai >= 75
    if nilai_siswa >= 75:
        print("Tuntas")
        # jika tuntas, kita hentikan perulangan 
        break
    else:
        #3. Jika tidak >=75, tanya apakah mau mengulang
        ulang = input("Apakah ingin mengulang? (Ya/Tidak): ")

        #4. cek jawaban mengulang
        if ulang == "ya":
            #Jika Ya, program akan kembali ke atas (input nilai)
            continue
        else:
            #5. Jika Tidak, cetak Tidak tuntas dan selesai 
            print("Tidak Tuntas")
            break 

        print("... program selesai ...")