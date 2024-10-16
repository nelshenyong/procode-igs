# Operasi Perbandingan Di Phyton
# 1. > Lebih Besar
# 2. < Lebih Kecil
# 3. >= Lebih Besar Sama Dengan
# 4. <= Lebih Kecil Sama Dengan
# 5. == Sama dengan
# 6. != Tidak sama dengan

a = float(input("Masukan nilai A: "))
b = float(input("Masukan nilai B: "))

# Operasi Lebih Besar
print(" ")
print("Lebih Besar")
print("----------->")
hasil = a > b
print(a, '>', b, "=", hasil)

print("----------->")
hasil = b > a
print(b, '>', a, "=", hasil)

# Operasi Lebih Kecil
print(" ")
print("Lebih Kecil")
print("----------->")
hasil = a < b
print(a, '<', b, "=", hasil)

print("----------->")
hasil = b < a
print(b, '<', a, "=", hasil)

# Operasi Lebih Besar Sama Dengan
print(" ")
print("Lebih Besar Sama Dengan")
print("----------->")
hasil = a >= b
print(a, '>=', b, "=", hasil)

print("----------->")
hasil = b >= a
print(b, '>=', a, "=", hasil)

# Operasi Lebih Kecil Sama Dengan
print(" ")
print("Lebih Kecil Sama Dengan")
print("----------->")
hasil = a <= b
print(a, '<=', b, "=", hasil)

print("----------->")
hasil = b <= a
print(b, '<=', a, "=", hasil)

# Operasi Sama Dengan
print(" ")
print("Lebih Kecil Sama Dengan")
print("----------->")
hasil = a == b
print(a, '==', b, "=", hasil)

print("----------->")
hasil = b == a
print(b, '==', a, "=", hasil)

# Operasi Sama Dengan
print(" ")
print("Lebih Kecil Sama Dengan")
print("----------->")
hasil = a != b
print(a, '!=', b, "=", hasil)

print("----------->")
hasil = b != a
print(b, '!=', a, "=", hasil)