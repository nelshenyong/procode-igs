#DICTIONARY => Assosiation Array
#Key, Value

#1.
data_dic1 = {
    'nama' : 'budi',
    'umur' : '15',
    'kelamin' : 'Laki - Laki',
    'alamat' : 'Palembang'
}

#2.
data_dic2 = dict(
    hewan = "ayam",
    jenis = "cemani",
    warna = "hitam"
)

#ambil value di dict
print(f"Data dict1, nama = {data_dic1['nama']}")
print(f"Data dict1, umur = {data_dic1.get('umur')}")
print(f"Data dict1, kelamin = {data_dic1.get('kelamin')}")
print(f"Data dict1, alamat = {data_dic1.get('alamat')}")

print("*"*25)

print(f"Data dict2, hewan = {data_dic2['hewan']}")
print(f"Data dict2, jenis = {data_dic2.get('jenis')}")
print(f"Data dict2, warna = {data_dic2.get('warna')}")
print(f"Data dict2, berat = {data_dic2.get('berat', 'tidak ditemukan')}")

#Membuat dict, dengan type data:
data_dic3 = dict(
    mobil = "Avanza", #ini string
    transmisi_auto = True, #ini boolean
    tahun = 2022, #ini int
    warna = ["Merah", "Hitam", "Putih"]
)

print("*"*25)
print(f"Data dic3 = {data_dic3}")
print(f"Warna = {data_dic3['warna']}")
print(f"Warna merah = {data_dic3['warna'][0]}")

print("*"*25)
#Menghitung value di dict
print(f"Jumlah key/data di dict {len(data_dic3)}")
print(f"Jumlah key/data di dict wrna merah {len(data_dic3['warna'][0])}")

print("*"*25)
cari_key1 = 'mobil' in data_dic3
print(f"Hasil cari key 1 - {cari_key1}")
cari_key2 = 'ban' in data_dic3
print(f"Hasil cari key 2 - {cari_key2}")

print("*"*25)
data_dic4 = dict(
    sd = "sd igs",
    #sd = "sd cgc", Tidak boleh key yang sama dalam satu dict
    smp = "smp igs",
    sma = "sma igs"
)

print("*"*25)
#Update data di dict
#1
data_dic5 = dict(
    film = "Avatar",
    tahun = 2022,
    genre = "Adventure"
)
print(f"Data ori dict5: {data_dic5}")
data_dic5["tahun"] = 2012
data_dic5["tgl_tayang"] = "15 Sep"
print(f"Data update dict5: {data_dic5}")

#2
data_dic5.update({"film" : "Marvel"})
print(f"Data update dict5: {data_dic5}")
data_dic5.update(dict(genre = "Action"))
print(f"Data update dict5: {data_dic5}")

print("*"*25)
#Hapus data di dict
print(f"Data ori dict5: {data_dic5}")
del data_dic5["genre"]
print(f"Data hapus dict5: {data_dic5}")
data_dic5.clear() #Ini akan menghapus semua key, value di dict
print(f"Data hapus semua dict5: {data_dic5}")


print("*"*25)
data_final = dict()
data_final.update({"status" : "selesai", "b.asing" : "coding"})
print(f"Data data_final = {data_final}")



































