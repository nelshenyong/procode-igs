print("<<< Penjualan di Toko XYZ >>>")

harga_barang = int(input("Harga Barang: Rp"))
qty = int(input("Jumlah Beli\t: "))

print(f"Harga Total\t: {harga_barang * qty}")

if qty >= 12 :
    diskon = 0.2 * (harga_barang * qty)
else: 
    diskon = 0

print(f"Diskon\t: Rp{diskon}")
print(f"Totall Bayar\t: Rp{(harga_barang * qty) - diskon}")