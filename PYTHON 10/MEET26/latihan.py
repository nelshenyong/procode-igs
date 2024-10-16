def bil_prima(bil): 
    if bil < 2:
        return False

    for i in range(2, int(bil ** 0.5) + 1):
        if bil % i == 0:
            return False

    return True

def ganjil(inputan_angka_awal, inputan_angka_akhir):
    data_ganjil = []
    for x in range(inputan_angka_awal, inputan_angka_akhir + 1):
        if x % 2 == 1:
            data_ganjil.append(x)
    return data_ganjil

def genap(inputan_angka_awal, inputan_angka_akhir):
    data_genap = []
    for y in range(inputan_angka_awal, inputan_angka_akhir + 1):
        if y % 2 == 0:
            data_genap.append(y)
    return data_genap
    
def show(inputan_angka_awal, inputan_angka_akhir):
    data_prima = []
    for i in range(inputan_angka_awal, inputan_angka_akhir + 1):
        if bil_prima(i):
            data_prima.append(i)
    return data_prima

while True:
    print("Pilihan: \n1. Bilangan Ganjil\n2. Bilangan Genap\n3. Bilangan Prima")
    pilihan = input("Pilih (1 / 2 / 3): ")

    if pilihan == "1":
        inputan_angka_awal = int(input("Masukan bilangan awal: "))
        inputan_angka_akhir = int(input("Masukan bilangan akhir: "))
        data_ganjil = ganjil(inputan_angka_awal, inputan_angka_akhir)
        print("Bilangan ganjil:", data_ganjil)

    elif pilihan == "2":
        inputan_angka_awal = int(input("Masukan bilangan awal: "))
        inputan_angka_akhir = int(input("Masukan bilangan akhir: "))
        data_genap = genap(inputan_angka_awal, inputan_angka_akhir)
        print("Bilangan genap:", data_genap)
        
    elif pilihan == "3":
        inputan_angka_awal = int(input("Masukan bilangan awal: "))
        inputan_angka_akhir = int(input("Masukan bilangan akhir: "))
        data_prima = show(inputan_angka_awal, inputan_angka_akhir)
        print("Bilangan prima:", data_prima)
    
    lanjut = input("Lanjut (Y/T): ").lower()
    if lanjut != "y":
        break
    
    
    
    
    