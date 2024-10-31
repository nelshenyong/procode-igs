print(">> Pendeteksi warna Lampu Lalu Lintas <<")

warna = (input("Masukkan Warna: "))

if warna.lower() == "merah":
    print("Berhenti!!")
elif warna.lower() == "hijau": 
    print("Jalan!!")
elif warna.lower() == "kuning":
    print("Hati - Hati!!")
else :
    print("Warna Tidak Sesuai!!")