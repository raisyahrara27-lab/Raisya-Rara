import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        kuantitas = int(entry_kuantitas.get())
        total = harga * kuantitas

        label_total.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Membuat window
window = tk.Tk()
window.title("Program Kasir")
window.geometry("300x250")
window.resizable(False, False)

# Frame utama
frame = ttk.Frame(window, padding=20)
frame.pack(expand=True)

# Label dan Entry Harga
label_harga = ttk.Label(frame, text="Harga:")
label_harga.pack()
entry_harga = ttk.Entry(frame)
entry_harga.pack(pady=5)

# Label dan Entry Kuantitas
label_kuantitas = ttk.Label(frame, text="Kuantitas:")
label_kuantitas.pack()
entry_kuantitas = ttk.Entry(frame)
entry_kuantitas.pack(pady=5)

# Tombol Hitung
btn_hitung = ttk.Button(frame, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=10)

# Label Total
label_total = ttk.Label(frame, text="Total: Rp.0.00", font=("Arial", 10, "bold"))
label_total.pack()

window.mainloop()