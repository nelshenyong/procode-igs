nama_global = "INI GLOBAL"

for i in range (1,5):
    print(f"{i}. {nama_global}")
    
def fungsi1():
    print(f"ini nama global di fungsi1 : {nama_global}")
    
print("\n")

fungsi1()

def fungsi2():
    nama_lokal = "INI LOCAL"
    
fungsi2()
# print(f"{nama_lokal}") // imi adalah variabel local!

def fungsi3():
    global lokal_diakses
    lokal_diakses = "local test"
    
fungsi3()
print(f"Fungsi 3: {lokal_diakses}")