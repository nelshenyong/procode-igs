def batas():
    print("-"*40)

def prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bilangan(awal, akhir, **kwargs):
    bilangan_prima = []
    bilangan_komposit = []

    for num in range(awal, akhir + 1):
        if prima(num):
            bilangan_prima.append(num)
        else:
            bilangan_komposit.append(num)

    if kwargs.get('tampilkan_prima',True):
        print('Bilangan prima\n',bilangan_prima)
    if kwargs.get('tampilkan_komposit',True):
        print('Bilangan komposit:\n',bilangan_komposit)

while True:
    print("<"*7, "BILANGAN PRIMA / KOMPOSIT")
    batas()
    print("1. Bilangan Prima 2. Blangan komposit")
    batas()
    pilihan = input('Pilihan ( 1-2 ): ')
    awal_angka = int(input('Masukkan angka awal: '))
    akhir_angka = int(input('Masukkan angka akhir: '))
    batas()
    if pilihan == '1':  
        bilangan(awal_angka, akhir_angka,tampilkan_prima=True,tampilkan_komposit=False)
    elif pilihan == '2':
        bilangan(awal_angka, akhir_angka,tampilkan_prima=False,tampilkan_komposit=True)
    batas()
    lanjut = input("Lanjut (y/t): ").lower()
    if lanjut != "y":
        break