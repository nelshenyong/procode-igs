x = 0
while x < 6:
    x += 1
    if x == 3:
        pass #Statement ini dummy(Dilewatkan saja), jadi tidak ada aksi
    print(x)

print("-"*27)
for i in range(1,5):
    if x == 2:
        pass
    print(i)

print("-"*27)
try:
    x = int(input("Masukkan nilai x: "))
    y = int(input("Masukkan nilai y: "))    
    print(f"Hasil penjumlahan: {x+y}")
except : pass

#Continue
i = 0
while i < 7:
    print(f"Nilai i: {i}")
    i += 1
    if i == 2:
        continue
        print("Lanjut...")
    print("Okey...")
print("Selesai...") 

print("-"*27)
for i in range(1,5):
    if i == 3:
        continue
    else:
        print(f"Nilai i in range(1,5): {i}")

#Break
print("-"*27)
for i in range(1,6):
    print(i)
    if i == 2:
        break