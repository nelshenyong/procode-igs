def bil_prima(bil): 
    data_prima = True
    if (bil == 0) or (bil == 1):
        data_prima = False
    else:
        for i in range(2, bil):
            if (bil % i == 0):
              data_prima = False
        return data_prima
inputan_angka_awal = int(input("Masukan bilangan awal: "))
inputan_angka_akhir = int(input("Masukan bilangan akhir: "))

        
def show(inputan_angka_awal, inputan_angka_akhir):
    data_prima = []
    for i in range (inputan_angka_awal, inputan_angka_akhir +1):
        if (bil_prima(i)):
            data_prima.append(i)
    return data_prima


print(show(inputan_angka_awal, inputan_angka_akhir))
