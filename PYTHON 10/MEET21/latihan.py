siswa1 = {
    'nm' : 'Effendi',
    'kelas' : 'X.10',
    'jk' : 'L',
    'mp' : 'Coding'
}
siswa2 = {
    'nm' : 'Dewi',
    'kelas' : 'X.9',
    'jk' : 'p',
    'mp' : 'DKV'
}
siswa3 = {
    'nm' : 'William',
    'kelas' : 'X.7',
    'jk' : 'L',
    'mp' : 'Mandarin'
}

data_siswa = {
    '1' : siswa1,
    '2' : siswa2,
    '3' : siswa3
}

print(f"Data siswa: {data_siswa}")

import os
os.system('cls')

print(f"{'NO':<5} {'NAMA':<15} {'KELAS':<10} {'KELAMIN':<10} {'MATA PELAJARAN':<20}")
print("-"*50)

for key, value in data_siswa.items():
    print(f"{key:<5} {value['nm']:<15} {value['kelas']:<10} {value['jk']:<10} {value['mp']:<20}")
print("-"*50)

print("FOR - KEYS")
for i in data_siswa.keys():
    print(f"{data_siswa[i]} {data_siswa[i]['nm']:<15} {data_siswa[i]['kelas']:<10} {data_siswa[i]['jk']:<10} {data_siswa[i]['mp']:<20}")
    
print("-"*50)
print("FOR VALUE")
kd = 1
for i in data_siswa.values():
    print(f"{'kd':<5} {i['nm']:<15} {i['kelas']:<10} {i['jk']:<10} {i['mp']:<20}")
    kd += 1
    
print("-"*50)
print("FOR")
for i in data_siswa:
    print(f"{data_siswa[i]} {data_siswa[i]['nm']:<15} {data_siswa[i]['kelas']:<10} {data_siswa[i]['jk']:<10} {data_siswa[i]['mp']:<20}")

