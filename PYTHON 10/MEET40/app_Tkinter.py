import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
show = tkinter.Tk()

show.title("Biodata") #Title
show.configure( bg = "Gray") #Background
show.geometry("300x300") #Size
show.resizable(True, True) #(X, Y) #Resize

frame = ttk.Frame(show)
#Pengaturan tampilan: pack, pad, place
frame.pack(padx=15, pady=15, fill="x", expand=True)

label_nama = ttk.Label(frame, text="Nama: ")
label_nama.pack(padx=10, pady=10, fill="x", expand=True)

varNama = tkinter.StringVar()

entry_nama = ttk.Entry(frame, textvariable=varNama)
entry_nama.pack(padx=10, pady=10, fill="x")


label_kelas = ttk.Label(frame, text="Kelas: ")
label_kelas.pack(padx=10, pady=10, fill="x", expand=True)

varKelas = tkinter.StringVar()

entry_kelas = ttk.Entry(frame, textvariable=varKelas)
entry_kelas.pack(padx=10, pady=10, fill="x")

def ActionSend():
    output = f"Halo, perkenalkan nama saya {varNama.get()} dari kelas {varKelas.get()}"
    showinfo(message=output)

submit = ttk.Button(frame, text="Kirim", command=ActionSend)
submit.pack(padx=10, pady=10, fill="x", expand=True)

show.mainloop()