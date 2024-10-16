# LAMBDA FUNCTION,

def batas():
    print("-"*30)

def tambah(angka):
    return angka+angka

print(f"Hasil function, def tambah: {tambah(4)}")

batas()

tambah_lambda = lambda angka: angka + angka
print(f"Hasil function, lambda tambah: {tambah_lambda(4)}")


batas()
data_list = ['ccc', 'cc', 'aaa', 'eee', 'dddd', 'e']
data_list.sort()
print(data_list)

batas()
def banyak_data(data):
    hasil = len(data)
    return hasil
data_list.sort(key = banyak_data)
print(f"Ini data sort dengan len: {data_list}")

batas()
data_list2 = ['wwww', 'rrr', 'gg', 'lll']
data_list2.sort(key = lambda x: len(x))
print(f"Ini data sort 2 dengan Len, Lambda: {data_list2}")