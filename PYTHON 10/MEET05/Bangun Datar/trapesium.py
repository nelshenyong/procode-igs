#Belah Ketupat
sisi_alas = float(input("Masukkan nilai Sisi Alas: "))
sisi_2 = float(input("Masukkan nilai Sisi 2: "))
sisi_3 = float(input("Masukkan nilai Sisi 3: "))
sisi_4 = float(input("Masukkan nilai Sisi 4: "))
tinggi = float(input("Masukkan nilai Tinggi: "))

keliling = sisi_alas + sisi_2 + sisi_3 + sisi_4
luas = ((sisi_alas + sisi_2) / 2) * tinggi

print("Keliling: ", keliling)
print("Luas: ", luas)