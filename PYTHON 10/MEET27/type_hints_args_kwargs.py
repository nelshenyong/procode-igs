def batas():
    print("="*20)
# Struktur, type hints
#     def nama_function(nama_argumen:tipe_data) -> tipe_data
batas()
def nama(data):
    print(f"Nama saya {data}")   
nama("admin")

batas()
def tambah_100(angka):
    hasil = 100 + angka
    return hasil
print(tambah_100(200))
# print(tambah_100("Nasi")) bermasalah karena argumen berbeda tipe data

batas()
def tambah_50(angka:int) -> int:
    hasil = 50 + angka 
    return hasil
print(tambah_50(25))

batas()
# args = argumen, args = argumn dinyatakan dengan simbol '*'
def siswa(nama, kelas, jurusan):
    return print(f"Nama saya {nama}, kelas {kelas}, jurusan {jurusan}")
siswa("Asep", "10", "Jadi lovel")

batas()
def siswa_sma(data):
    nama = data[0]
    kelas = [1]
    jurusan = data[2]
    return print(f"Nama saya {nama}, kelas {kelas}, jurusan {jurusan}")
siswa_sma(["Kona", "11", "Jadi sapu terbang"])

batas()
def siswa_smp(*data):
    nama = data[0]
    kelas = [1]
    jurusan = data[2]
    return print(f"Nama saya {nama}, kelas {kelas}, jurusan {jurusan}")
siswa_sma(["Kona", "11", "Jadi sapu terbang"])
    
    
batas()
def tambahan(*data):
    angka = 0
    for i in data:
        angka += 1
        return angka
print(tambahan(4,5,7,3))

batas()
def daftar_siswa(*data):
    print("Daftar siswa: ")
    for i, value in enumerate(data):
        print(f"{i}. {value}")
        i+=1
daftar_siswa("budi", "indah", "ani")

batas()
def hewan(*data):
    return data

data_hewan = hewan("Calvin", "Patrick", "Immanuel", "Mario", "Winata", "Reagen")
print(data_hewan)
print(type(data_hewan))