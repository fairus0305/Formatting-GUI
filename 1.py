import tkinter as tk

# Fungsi hasil prediksi
def hasil_prediksi():
    
    popup = tk.Toplevel(root)
    popup.title("Hasil Prediksi")
    popup.geometry("420x150")

    label_hasil = tk.Label(
        popup,
        text="Prediksi Prodi: Teknologi Informasi",
        font=("Arial", 14, "bold")
    )
    label_hasil.pack(expand=True)



root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x720")


label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold")
)
label_judul.pack(pady=20)


frame_input = tk.Frame(root)
frame_input.pack()

list_entry = []

for i in range(10):
    label_nilai = tk.Label(
        frame_input,
        text="Nilai Mata Pelajaran " + str(i + 1) + ":",
        font=("Arial", 12)
    )
    label_nilai.grid(
        row=i, column=0,
        sticky="e", padx=10, pady=4
    )

    entry_nilai = tk.Entry(
        frame_input,
        width=20,
        font=("Arial", 10, "bold")
    )
    entry_nilai.grid(
        row=i, column=1,
        sticky="w", padx=10, pady=4
    )

    list_entry.append(entry_nilai)



label_jurusan = tk.Label(
    root,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 12)
)