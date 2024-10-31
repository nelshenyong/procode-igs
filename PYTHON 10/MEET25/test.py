def header():
    import os
    os.system("cls")
    
    print("/"*25)
    
def head():
    print("/"*25)
    
def inputan():
    inputan_angka = int(input("Masukan bilangan: "))
    return inputan_angka

def bil_prima(bil): 
    data_prima = True
    if (bil == 0) or (bil == 1):
        data_prima = False
    else:
        for i in range(2, bil):
            if (bil % i == 0):
              data_prima = False
        return data_prima
    
    
while True:        
    header()
    angka = inputan()

    if (bil_prima(angka)):
        print(f"Angka {angka} adalah bilangan prima!")
    else:
        print(f"Angka {angka} adalah bukan bilangan prima!")
        
    opsi = input("Lanjutkan (Y/T): ")
    if opsi.lower() == 't':
        print("Dihentikan!")
        break
    