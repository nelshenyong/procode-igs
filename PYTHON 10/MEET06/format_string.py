# Operasi format String di python
# 1. %
# 2. str.format
# 3. f.format

print("Format string dengan %")

nama = "Nelshen Yong" #string -> s
usia = 15 #integer #integer -> i / n
u_sepatu = 45 #float -> f

print("String")
print("Halo nama saya %s, usia saya %i, ukuran sepatu saya %0.3f" %(nama, usia, u_sepatu))

print("str.format")
print("Halo nama saya {0}, usia saya {1}, ukuran sepatu saya {2}, kelamin saya {jk}" .format(nama, usia, u_sepatu, jk="Laki-Laki"))

print("Nama : [{nm:20}]" .format(nm="Nelshen"))
print("Nama : [{nm:>20}]" .format(nm="Nelshen"))
print("Nama : [{nm:<20}]" .format(nm="Nelshen"))
print("Nama : [{nm:^20}]" .format(nm="Nelshen"))

print("f.format")
print(f"Halo nama saya {nama}, usia saya {usia}, ukuran sepatu saya {u_sepatu}")
print(f"Nama : [{nama:>20}]")
print(f"Nama : [{nama:<20}]")
print(f"Nama : [{nama:^20}]")
