from datetime import date

print(">> Menghitung Usia <<")
print("Masukan tanggal, bulan, tahun lahir")

tanggal = int(input("Masukan tanggal lahir\t: "))
bulan = int(input("Masukan bulan lahir\t: "))
tahun = int(input("Masukan tahun lahir\t: "))
hari_ini = date.today()

tgl_kelahiran = date(tahun, bulan, tanggal)

print(f"Tanggal kelahiran anda adalah {tanggal}")
print(f"Tanggal hari ini adalah {hari_ini}")

umur = hari_ini - tgl_kelahiran
umur_tahun = umur.days // 365
umur_bulan = (umur.days % 365) // 30
umur_hari = (umur.days % 365) % 31

print(f"Umur anda adalah: {umur_tahun} Tahun, {umur_bulan} Bulan, {umur_hari} Hari")