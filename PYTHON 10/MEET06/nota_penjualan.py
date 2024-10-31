nama_barang = str(input("Masukkan Nama barang: "))
harga_barang = int(input("Masukkan Harga barang: "))
jumlah_barang = int(input("Masukkan Jumlah barang: "))
diskon_barang = int(input("Masukkan Diskon barang: "))

sub_total = harga_barang * jumlah_barang
diskon = (sub_total * diskon_barang) / 100
total_bayar = sub_total - diskon

print("[{nm:^20}]" .format(nm=">>>   Nota Pembelian - Toko xyz   <<<"))
print("{nm:^20}" .format(nm="-"*39))
print("{nm:<20}" .format(nm="Nama barang: %s") %(nama_barang))
print("{nm:<20}" .format(nm="Harga barang: Rp%s") %(harga_barang))
print("{nm:<20}" .format(nm="Jumlah Barang: %s") %(jumlah_barang))
print("{nm:<20}" .format(nm="Diskon : Rp%s") %(diskon))
print("{nm:<20}" .format(nm="Total: Rp%s") %(total_bayar))

print("{nm:^20}" .format(nm=f"-"*39))

jumlah_uang = int(input("Jumlah Uang: "))

kembalian = jumlah_uang - total_bayar
print("Rincian Kembalian: ")

print(f"Kembalian: Rp{kembalian}")

lembar_50rb = kembalian // 50000
print(f"50.000: {lembar_50rb} Lembar")

sisa_kembalian20 =  lembar_50rb % 20000
lembar_20rb = sisa_kembalian20 // 20000
print(f"20.000: {lembar_20rb} Lembar")

sisa_kembalian10 =  lembar_20rb % 10000
lembar_10rb = sisa_kembalian10 // 10000
print(f"10.000: {lembar_10rb} Lembar")

sisa_kembalian5 =  lembar_10rb % 5000
lembar_5rb = sisa_kembalian5 // 5000
print(f"5.000: {lembar_5rb} Lembar")

sisa_kembalian2 =  lembar_5rb % 2000
lembar_2rb = sisa_kembalian2 // 2000
print(f"2.000: {lembar_2rb} Lembar")

sisa_kembalian1 =  lembar_2rb % 1000
lembar_1rb = sisa_kembalian1 // 1000
print(f"2.000: {lembar_1rb} Lembar")