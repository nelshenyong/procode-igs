def batas():
    print("-"*25)
    
def header():
    import os
    os.system("cls")
    print("-"*15, "MODUS", "-"*15)
    
def inputan():
    while True:
        try:
            input_angka = int(input("Masukan angka: "))
            break
        except ValueError:
            print("Masukan angka!!")
            continue
    return input_angka

def data_modus(**data):
    data_muncul = {}
    
    for i in data ["nilai"]:
        if i in data_muncul:
            data_muncul.update({i : data_muncul[i] +1})
        else:
            data_muncul.update({i : 1}) 
    angka_max = max( data_muncul.values())
    daftar_modus = []
    for key, value in data_muncul. items():
        if value == angka_max:
            daftar_modus.append(key)
        return daftar_modus
    
    
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
hasil_modus = data_modus(nilai = daftar_angka)
print(f"Modus dari data {sorted(daftar_angka)} = {hasil_modus}")