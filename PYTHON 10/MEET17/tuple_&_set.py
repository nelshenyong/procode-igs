data_list = [1, 4, 3, 5]
print(f"{data_list[0]}")

data_tuple = (3,4,2,3)
print(f"{data_tuple[0]}")

data_set = {2,1,3,5} 
# print(f"{data_set[0]}") (Tidak bisa)

print("\n << TAMBAH  VALUE: ")
data_list.insert(0, "igs")
print(f"Data list ditambah: {data_list}")
data_set.add("igs")
print(f"Data list update: {data_list}")
#data_tuple.add("igs") => data tuple tidak bisa ditambah

print("\n << UPDATE VALUE")
data_list[0] = "igs keren"
print(f"Data list update: {data_list}")

print("\n << HAPUS VALUE")
data_list.remove("igs keren")
print(f"Data list hapus: {data_list}")
data_set.remove(5)
print(f"Data set dihapus: {data_set}")

print("\n << Perulangan di tuple: ")

for i in data_tuple:
    print(f"Data tuple: {i}")

print("\n << PERULANGAN DI SET: ")

for i in data_set:
   print(f"Data set : {i}")