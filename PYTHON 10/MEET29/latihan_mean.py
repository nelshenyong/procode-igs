def batas():
    print("-"*35)
    
def header():
    import os
    os.system("cls")
    
def inputan():
    while True:
        try:
            input_data = int(input("Masukan angka: "))
            break
        except ValueError:
            print("Masukan angka!")
            continue
    return input_data

def mean(**data):
    data_value = data["nilai"]
    jum_data = sum(data["nilai"])
    bnyk_data = len(data["nilai"])
    hasil = round((jum_data / bnyk_data),2)
    return hasil

#Main - mini project 
daftar_angka = []
while True:
    batas()
    header()
    daftar_angka.append(inputan())
    opsi = input("Lanjut (y/t): ").lower()
    
    if(opsi  == "t"):
        break
batas()
header()
print(f"Hasil mean dari data: {daftar_angka} = {mean(nilai = daftar_angka)}")