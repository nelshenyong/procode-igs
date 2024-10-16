class Mobil():
    #class variabel
    jumlah_mobil = 0
    def __init__(self, nama, warna, kecepatan):
        #instance varibel
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        Mobil.jumlah_mobil += 1
        
    def mobil(self):
        print(f"Mobil: {self.nama}")
        
    def ubah_warna(self, warna_baru):
        self.warna = warna_baru
        
    def tampil_warna(self):
        return print(f"Warna mobil {self.warna}")
    
print(f"Jumlah objek sebelum ditambah: {Mobil.jumlah_mobil}")
innova = Mobil('Innvona', 'Hitam', 300)
print(f"Jumlah objek setelah ditambah 1: {Mobil.jumlah_mobil}\n")

print(f"Jumlah objek sebelum ditambah: {Mobil.jumlah_mobil}")
fortuner = Mobil('Fortuner', 'Biru', 250)
print(f"Jumlah objek setelah ditambah 1: {Mobil.jumlah_mobil}\n")

print(f"Jumlah objek sebelum ditambah: {Mobil.jumlah_mobil}")
xpander = Mobil('Xpander', 'Abu', 200)
print(f"Jumlah objek setelah ditambah 1: {Mobil.jumlah_mobil}\n")

print(f"Atribut | Nama: {innova.nama}, Warna: {innova.warna}, Kecepatan: {innova.kecepatan}")
print(f"Atribut | Nama: {fortuner.nama}, Warna: {fortuner.warna}, Kecepatan: {fortuner.kecepatan}")
print(f"Atribut | Nama: {xpander.nama}, Warna: {xpander.warna}, Kecepatan: {xpander.kecepatan}")

fortuner.mobil()
fortuner.ubah_warna("Putih")
fortuner.tampil_warna()