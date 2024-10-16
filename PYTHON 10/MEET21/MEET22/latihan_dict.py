# dict.

# 1
# template = {
#     'nm' : '',
#     'mp' : '',
#     'k' : ''
# }

# daftar = dict.fromkeys(template.keys())

# daftar['nm'] = input("Nama \t:")
# daftar['mp'] = input("Mata Pelajaran \t:")
# daftar['k'] = input("Kelas \t:")

# data = {'Siswa' : daftar}
# print(data)

print("="*30)
import random
kd1 = random.randint(1, 200)
print(kd1)

print("="*30)
import string
kd2 = string.ascii_uppercase
print(kd2)

print("="*30)
data_01 = ('nm_brg', 'jenis', 'harga')
data_brg = dict.fromkeys(data_01)
data_brg['nm_brg'] = input("Nama Barang \t:")
data_brg['jenis'] = input("Jenis Barang \t:")
data_brg['harga'] = input("Harga Barang \t:")
kode = ' '.join(random.choice(string.ascii_uppercase) for i in range(5))

data_barang = {
    'kode' : data_brg,
}

print("-"*50)
print(f'{"Kode":<7} {"Barang":<20} {"Jenis":<15} {"Harga":<20}')
print("-"*50)
for key, value in data_barang.items():
    print(f"{key:<7} {value['nm_brg']:<20} {value['jenis']:<15} {value['harga']:<20}")