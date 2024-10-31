print("MEMBUAT ANGKA DALAM RANGE")

nilai_awal = int(input("Masukan nilai awal: "))
nilai_akhir = int(input("Masukan nilai akhir: "))

def angka(x, y):
    data_angka = []
    for i in range(x, y +1):
        data_angka.append(i)
    return data_angka
        
hasil = angka(nilai_awal, nilai_akhir)
print(f"Hasil data angka {nilai_awal} s/d {nilai_akhir} = {hasil}")



def ganjil(a, b):
    data_ganjil = []
    for x in range(a, b):
     if (x % 2 == 1):
        data_ganjil.append(x)
    return data_ganjil
        
print(f"Hasil data angka {nilai_awal} s/d {nilai_akhir} = {ganjil(nilai_awal, nilai_akhir)}")



def genap(c, d):
    data_genap = []
    for y in range(c, d):
     if (y % 2 == 0):
        data_genap.append(y)
    return data_genap
        
print(f"Hasil data angka {nilai_awal} s/d {nilai_akhir} = {genap(nilai_awal, nilai_akhir)}")