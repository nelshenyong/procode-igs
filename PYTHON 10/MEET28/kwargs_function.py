# kwargs = keyword argument, untk argumennya di tandai dengan **

def batas():
    print("-"*25)
    
def guru(**data):
    return data
hasil = guru(nama = 'Nelshen', mapel = 'Coding', kelas = '10')

# kesimpulan kwargs akan menghasilkan data dictionary
print(hasil)
print(type(hasil))

batas()
def materi(**data):
    print("Daftar materi kelas coding: ")
    no = 0
    for key, value in data.items():
        print(f"{no+1}. {value}")
        no += 1
    return 0

materi(meet1 = "List", meet2 = "Set", meet3 ="Tuple", meet4 = "Dictionary")


batas()
# arg = nom keyword
# kworgs = keyword 
def campuran(argumen1, argumen2, *arg, **kwargs):
    return argumen1, argumen2, arg, kwargs

h_argumen1, h_argumen2, h_args, h_kwargs = campuran(2,3,4,5,6,7,8,10, nila11 = 11, nilai12 = 12)
print(f"Argumen 1: {h_argumen1}")
print(f"Argumen 2: {h_argumen2}")
print(f"Args: {h_args}")
print(f"Kwargs: {h_kwargs}")

batas()
#def campuran_2 (**kwargs, argumen) kwargs tidak bisa dibuat pada awal argumen,harus setelah argumen standar dan args, dan juga args (non keyword) harus setelah standar argumen dan sebelum kwargs

#def campuran_3 (*args_1, *args_2, **kwargs_!, **kwargs_2) tidak boleh