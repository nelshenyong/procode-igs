#Jika nilai atas 5 dan nilai dibawah 8, maka benar

inputan = int(input("Masukan nilai: "))

cek1 = inputan > 5 #Hasil harus True, untuk benar
cek2 = inputan < 8 #Hasil harus True, untuk benar

hasil = cek1 and cek2

print('Nilai yang dimasukkan adalah: ', hasil)