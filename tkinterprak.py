import tkinter as tk
import tkinter.messagebox as msg

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("400x500")
top.configure(bg="#9800DE")

for i in range(10):
    nilai = tk.Frame(top, bg="#9800DE")
    nilai.pack(pady=4, padx=12)

    L1 = tk.Label(nilai, text=f"Nilai {i+1}: ", bg="#FFFFFF", width=8)
    L1.pack(side=tk.LEFT)

    E1 = tk.Entry(nilai, bd=6)
    E1.pack(side=tk.LEFT, expand=True)

tombolHasil = tk.Button(top, text="Hasil Prediksi", bg="#1198C5")
tombolHasil.pack(pady=20)

luaran = tk.Label(top, text="Luaran hasil prediksi")
luaran.pack(side=tk.BOTTOM)

top.mainloop()