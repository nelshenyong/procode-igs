print(">> KALKULATOR <<")
print("-"*20)
print("JURUSAN:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus")
print("-"*20)

kalkulator = int(input("Pilih jurusan (1 / 2 / 3 / 4 / 5): "))
a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

if kalkulator == 1:
    print(">> Penjumlahan <<")
    print(f"Hasil: {a + b}")
elif kalkulator == 2:
    print(">> Pengurangan <<")
    print(f"Hasil: {a - b}")
elif kalkulator == 3:
    print(">> Perkalian <<")
    print(f"Hasil: {a * b}")
elif kalkulator == 4:
    print(">> Pembagian <<")
    print(f"Hasil: {a / b}")
elif kalkulator == 5:
    print(">> Modulus <<")
    print(f"Hasil: {a % b}")
else :
    print("Pilihan Tidak Tersedia!")