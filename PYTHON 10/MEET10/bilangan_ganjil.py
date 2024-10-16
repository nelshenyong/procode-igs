print("<<<\tIDENTIFIKASI BILANGAN GANJIL\t>>>")

bil = int(input("Masukkan Bilangan Genap: "))

while 1 % 2 == 0: 
    print("Salah!")
    bil = int(input("Masukkan bilangan ganjil: "))
else:
    print("Benar!")