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

