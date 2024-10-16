import package
import os
os.system("cls")

while True:
    print("<"*7, "KONVERSI SATUAN HITUNGAN")
    jumlah_barang = int(input("Masukan jumlah barang\t: "))
    hasil = package.konversi_barang(jumlah_barang)
    package.batas()
    print(f"({hasil[0]}) gross, ({hasil[1]}) kodi, ({hasil[2]}) lusin, dan ({hasil[3]}) buah")
    package.batas()
    lanjut = input("Lanjut (y/t) : ").lower()
    if lanjut == 'y':
        print("-" * 50)
        continue
    else:
        break