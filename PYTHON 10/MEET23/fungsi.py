# fungsi / function / methodd
# merupakan blok kode yang terorganisir yang digunakan berulang kali, setiap kita butuh
# struktur:
    # def nama_fungsi():
    #     body_funsgsi
def hei():
    print("Selamat datang!")
hei()
hei()

def batas():
    print("+"*40)
batas()

# fungsi, dengan argumen
# struktur:
#     def nama_fungsi(argumen):
#         body_fungsi
def siswa(nama, kelas):
    print(f"nama saya {nama} di kelas {kelas}")
siswa('budi', '10.6')
batas()

def mtk(angka_1, angka_2, angka_3):
    print(f"Hasil dari {angka_1} + {angka_2} - {angka_3} = {angka_1 + angka_2 - angka_3}")
mtk(10,2,3)
mtk(10,5,-7)

batas()
def presensi(hadir):
    daftar_hadir = hadir.copy()
    print("Daftar kehadiran, Sabtu, 23 Sep 2023: ")
    no = 1
    for i in daftar_hadir:
        print(f"{no}. {i}")
        no += 1

siswa_hadir = ["Jati", "Iksan", "Venita", "Vincent"]

presensi(siswa_hadir)

batas()
# fungsi, dengan return / kembalian
# why return is needed?
def tambah(x,y):
    print(f"Hasilnya {x+y}")
    hasil = print("berhasil!")
    
hasil_1 = tambah(3,6)

batas()
def modulo(a,b):
    hasil = a % b
    return hasil

hasil_fix = modulo(6,7)
print(hasil_fix)
# Jadi kesimpulan return:
# INPUT -> FUNGSI -> OUPUT

batas()
# multi return
def tambah(a1,a2):
    return a1 + a2

hasil_tambah = tambah(7,9)
print(hasil_tambah)

batas()
# banyak output - input
def aritmatika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    bagi = angka_1 / angka_2
    kali = angka_1 * angka_2
    modulo = angka_1 % angka_2
    div = angka_1 // angka_2
    
    return tambah, kurang, bagi, kali, modulo, div
hasil = aritmatika(20, 2)
print(hasil)

batas()

h_tambah, h_kurang, h_bagi, h_kali, h_modulo, h_div = aritmatika (20, 2)
print(f"Hasil dari tambah: {h_tambah}")
print(f"Hasil dari kurang: {h_kurang}")
print(f"Hasil dari bagi: {h_bagi}")
print(f"Hasil dari kali: {h_kali}")
print(f"Hasil dari modulo: {h_modulo}")
print(f"Hasil dari div: {h_div}")
 
batas()

def pangkat(x, y):
    print(f"Hasilnya adalah {x**y}")
pangkat(2,6)

def pangkat_return(x, y):
    hasil = x**y
    return hasil

print(f"Hasil 1: {pangkat_return(10,2)}")
# Return bisa memproses nilai kembalian
print(f"Hasil 2: {pangkat_return(10,2)}")
# Tanpa return tidak bisa memproses nilai kembalian / return
# hasil = pangkat(10, 2) + 5

batas()
# Default value , argumen di fungsi
def motor(brand = "Honda", type = "Vario 160 CBS"):
    return print(f"Saya memiliki motor {brand} {type}")

motor()
motor(type = "Beat Street")

batas()
def mobil(brand, type):
    return print(f"Saya memiliki mobil {brand}, {type}")
# Ini tidak bisa karena tidak memiliki default / argumen value
# mobil()

batas()
def tambah(input_1 = 1, input_2 = 2, input_3 = 3, input_4 = 4):
    hasil = input_1 + input_2 + input_3 + input_4
    return hasil

print(tambah())
print(tambah(input_4 = 10))

