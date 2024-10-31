def batas():
    print("_"*30)
    
def header():
    print("<"*15, "ARITMATIKA dengan (args, kwargs)")
    import os
    os.system('cls')
    
def inputan():
    angka1 = int(input("Masukan angka 1\t: "))
    angka2 = int(input("Masukan angka 2\t: "))
    return angka1, angka2

def aritmatika(*angka, **pilihan):
    if(pilihan["opsi"] == "+"):
        hasil = angka[0] + angka[1]
    elif(pilihan["opsi"] == "-"):
        hasil = angka[0] - angka[1]
    elif(pilihan["opsi"] == "*"):
        hasil = angka[0] * angka[1]
    elif(pilihan["opsi"] == "/"):
        hasil = angka[0] / angka[1]
    elif(pilihan["opsi"] == "%"):
        hasil = angka[0] % angka[1]
    else:
        print("Salah!")
    return hasil
        
#main, mini project:
while True:
    header()
    print("Pilihan: (+, -, *, /, %)")
    operasi = input("Masukan pilihan operasi: ")
    angka1, angka2 = inputan()

    hasil_operasi = aritmatika(angka1, angka2, opsi = operasi)
    print(f"Hasilnya {hasil_operasi}")
    
    opsi = input("Lanjutkan (y/t): ").lower()
    if (opsi == "t"):
        break