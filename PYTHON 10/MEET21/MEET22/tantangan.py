import random
import string
import os

os.system('cls')
i = 0
data_mp = []
while True:
    data_01 = ('mata pelajaran', 'guru', 'hari', 'jam', 'ruangan')
    data = {}
    for key in data_01:
        data[key] = input(f"{key.capitalize()}\t: ")
    lanjut = input("Lanjut (Y/N)? ").lower()
    kode = ''.join(random.choices(string.ascii_uppercase, k=3))
    i += 1
    data_mp.append({
        'kode': kode,
        'data': data,
    })
    if lanjut == 'y':
        print("-" * 50)
        continue
    if lanjut == 'n':
        print(f'{"ID":<7} {"Mata Pelajaran":<20} {"Guru":<15} {"Hari":<5} {"Jam":<5} {"Ruangan":<10}')
        print("-" * 50)
        for key, value in enumerate(data_mp, start=1):
         print(f"{value['kode']:<7} {value['data']['mata pelajaran']:<20} {value['data']['guru']:<15} {value['data']['hari']:<5} {value['data']['jam']:<5} {value['data']['ruangan']:<10}")
        break
    else:
        print("Invalid input! (Retry)")
        break
    
    
    
    