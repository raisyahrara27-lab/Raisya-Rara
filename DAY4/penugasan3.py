import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = {
        "Nama Lengkap": entry_nama.get(),
        "Tanggal Lahir": entry_tgl.get(),
        "Asal Sekolah": entry_sekolah.get(),
        "NISN": entry_nisn.get(),
        "Nama Ayah": entry_ayah.get(),
        "Nama Ibu": entry_ibu.get(),
        "No HP": entry_hp.get(),
        "Alamat": text_alamat.get("1.0", tk.END).strip()
    }
    
    messagebox.showinfo("Data Tersimpan", f"Data berhasil disimpan!\n\n{data}")

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Window utama
root = tk.Tk()
root.title("Program Data Siswa")
root.geometry("500x600")
root.configure(bg="#b2ebf2")

# Frame utama
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=20)

# Judul
judul = tk.Label(frame, text="DATA SISWA BARU",
                 font=("Arial", 16, "bold"),
                 bg="#b2ebf2", pady=10)
judul.grid(row=0, column=0, columnspan=2, sticky="ew")

# Fungsi buat label + entry
def buat_label_entry(text, row):
    label = tk.Label(frame, text=text, anchor="w")
    label.grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame, width=40)
    entry.grid(row=row+1, column=0, columnspan=2, pady=5)
    return entry

entry_nama = buat_label_entry("Nama Lengkap", 1)
entry_tgl = buat_label_entry("Tanggal Lahir", 3)
entry_sekolah = buat_label_entry("Asal Sekolah", 5)
entry_nisn = buat_label_entry("NISN", 7)
entry_ayah = buat_label_entry("Nama Ayah", 9)
entry_ibu = buat_label_entry("Nama Ibu", 11)
entry_hp = buat_label_entry("Nomor Telepon / HP", 13)

# Alamat (Text)
label_alamat = tk.Label(frame, text="Alamat", anchor="w")
label_alamat.grid(row=15, column=0, sticky="w", pady=5)

text_alamat = tk.Text(frame, width=40, height=4)
text_alamat.grid(row=16, column=0, columnspan=2, pady=5)

# Tombol
btn_hapus = tk.Button(frame, text="Hapus", bg="#e67e22",
                      fg="white", width=10, command=hapus_data)
btn_hapus.grid(row=17, column=0, pady=20)

btn_simpan = tk.Button(frame, text="Simpan", bg="#e67e22",
                       fg="white", width=10, command=simpan_data)
btn_simpan.grid(row=17, column=1, pady=20)

root.mainloop()