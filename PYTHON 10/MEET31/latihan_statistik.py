def batas():
    print("-"*25)
    
def header():
    import os
    os.system("cls")
    print("-"*15, "STATISTIK", "-"*15)
    
def inputan():
    while True:
        try:
            input_angka = int(input("Masukan angka: "))
            break
        except ValueError:
            print("Masukan angka!!")
            continue
    return input_angka

def statistik(**data):
    import statistics
    hasil_mean = statistics.mean(data["nilai"])
    hasil_median = statistics.median(data["nilai"])
    hasil_modus = statistics.multimode(data["nilai"])
    return hasil_mean, hasil_median, hasil_modus



daftar_angka = []
while True:
    batas()
    header()
    daftar_angka.append(inputan())
    opsi = input("Lanjutkan (y/t) \t:")
    if(opsi.lower() == "t"):
        break
    
batas()
header()
nilai_mean, nilai_median, nilai_modus = statistik(nilai = daftar_angka)
print(f"Daftar data {sorted(daftar_angka)}")
print(f"Mean = {nilai_mean}")
print(f"Median = {nilai_median}")
print(f"Modus = {nilai_modus}")