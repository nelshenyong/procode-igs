inputan = int(input("Masukan nilai: "))

cek1 = inputan > 5 #Hasil harus True, untuk benar
cek2 = inputan < 8 #Hasil harus True, untuk benar
cek3 = inputan > 14 #Hasil harus True, untuk benar
cek4 = inputan < 20 #Hasil harus True, untuk benar

hasil = cek1 and cek2 or cek3 and cek4

print('Nilai yang dimasukkan adalah: ', hasil)