print(">> Daftar Tiket <<")
print("-"*20)
print("JURUSAN:")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuk Linggau")
print("-"*20)

tiket = int(input("Pilih jurusan (1 / 2 / 3): "))

if tiket == 1:
    print("Tiket ke Prabumulih Rp150.000")
    prabumulih = int(input("Jumlah Tiket: "))
    print(f"Total harga tiket: Rp{prabumulih * 150000}")
elif tiket == 2:
    print("Tiket ke Muara Enim Rp300.000")
    muara_enim = int(input("Jumlah Tiket: "))
    print(f"Total harga tiket: Rp{muara_enim * 300000}")
elif tiket == 3:
    print("Tiket ke Lubuk Linggau Rp400.000")
    lubuk_linggau = int(input("Jumlah Tiket: "))
    print(f"Total harga tiket: Rp{lubuk_linggau * 400000}")
else :
    print("Pilihan Tidak Tersedia!")