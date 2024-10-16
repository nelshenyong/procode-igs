# Ambil item/value dalam list
#               0/-3       1/-2      2/-1
data_list = ["Ignatius", "Global", "School"]
print(f"Data list 0: {data_list[0]}")
print(f"Data list -2: {data_list[-2]}")

print("-"*35)
# Ambil tertentu di value list
#             0/-6 1/-5 2/-4 3/-3 4/-2 5/-1
data_list2 = [ 1,   2,   3,   4,  "a",  "b"]
print(f"Data list 2 [1:3]: {data_list2[1:3]}")
print(f"Data list 3 [2:-1]: {data_list2[2:-1]}")
print(f"Data list 4 [3:]: {data_list2[3:]}")
print(f"Data list 5 [:3]: {data_list2[:3]}")

print("-"*35)
#Mengabungkan list
data1 = [223, 3232, 2324, 2451, 7655, 5363]
data2 = ["A", "B", "C", 'D']
print(f"Hasil gabung data1, data2: {data1 + data2}")

data1.extend(data2)
print(f"Hasil gabung extend: {data1}")

#Menghitung jumlah value dalam list: len
print(f"Jumlah value/item di data1: {len(data1)}")

print("-"*35)
#Repition
data3 = ["x", "y"] * 20
print(f"Jumlah value/item di data3: {data3}")

print("-"*35)
# Member in list
data4 = ["kuning", "merah", "hijau"]
if "kuning" in data4:
    print("Benar")
else:
    print("Salah")

print("-"*35)
#List dalam perulangan

for i in ["ayam", "anjing", "kucing"]:
    print(f"Value dari i: {i}")

print("-"*35)
#Menambahkan value dalam list
data_list.insert(0, "SMA")
print(f"Data list setelah diinsert: {data_list}")

data_list.append("oke")
print(f"Data list setelah diappend: {data_list}")

#Mengupdate value dalam list
print("-"*35)
data_list[-1] = "keren"
print(f"Data list setelah diupdate: {data_list}")

#Menghapus value dalam list
print("-"*35)
data_list.remove("SMA")
print(f"Data list setelah diremove: {data_list}")

# value dalam list
print("-"*35)
data_list.pop()
print(f"Data list setelah dipop: {data_list}")

# Mencari posisi value
print("-"*35)
data_num = [32,24412,241,14,124,214,1535,244,346,6534,1435,1436,35462,325262,236236,252,214,252,214]
data_list.index
print(f"Value 1535 dalam list num ada di posisi: {data_num.index(1535)}")
print(f"Value 24412 dalam list num ada di posisi: {data_num.index(24412)}")

# Menghitung jumlah value dalam list
print("-"*35)
print(f"Jumlah item 214 dalam list adalah: {data_num.count(214)}")
print(f"Jumlah item 252 dalam list adalah: {data_num.count(252)}")

# Mencari value terbesar dan terkecil dalam list
print("-"*35)
print(f"Data terkecil dalam list adalah {min(data_num)}")
print(f"Data terbesar dalam list adalah {max(data_num)}")

# Mengurutkan data dalam list
print("-"*35)
data_num.sort()
print(f"Data list setelah di sort {data_num}")
data_num.reverse()
print(f"Data list setelah di reverse {data_num}")