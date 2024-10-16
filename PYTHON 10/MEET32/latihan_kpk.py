a = int(input("Masukan angka pertama: "))
b = int(input("Masukan angka kedua: "))
c = b
d = a

hasil_modulus = a % b
hasil_modulus1 = c % d

hasil = lambda x, y : x % y

while True: 
    if ((hasil(hasil_modulus, a) == 0) and (hasil(hasil_modulus, b) == 0)):
        break
    if ((hasil(hasil_modulus1, c) == 0) and (hasil(hasil_modulus1, d) == 0)):
        break
    
    hasil_modulus += a
    hasil_modulus1 += c
    
print(f"Hasil KPK dari {a}, {b} : {hasil_modulus}")
print(f"Hasil KPK dari {c}, {d} : {hasil_modulus1}")