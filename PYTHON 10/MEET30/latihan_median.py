def batas():
    print("-"*25)
    
def header():
    import os
    os.system("cls")
    print("-"*15, "MEDIAN", "-"*15)
    
def inputan():
    while True:
        try:
            input_angka = int(input("Masukan angka: "))
            break
        except ValueError:
            print("Masukan angka!!")
            continue
    return input_angka

def median(**data):
    data_sort = sorted(data["nilai"])
    jml_angka = len(data["nilai"])
    if (jml_angka % 2 == 1): #Kondisi ganjil
        hasil_median = data_sort[jml_angka // 2]
    else: #Kondisi ganjil
        proses1 = data_sort[jml_angka // 2]
        proses2 = data_sort[(jml_angka // 2) - 1]
        hasil_median = (proses1 + proses2) / 2
    return hasil_median


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
hasil_median_final = median(nilai = daftar_angka)
print(f"Median dari data {sorted(daftar_angka)} adalah {hasil_median_final}")

