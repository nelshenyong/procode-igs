print("<<<\tIDENTIFIKASI BILANGAN GENAP\t>>>")

bil = int(input("Masukkan Bilangan Genap: "))

while bil % 2 == 1: 
    print("Salah!")
    bil = int(input("Masukkan bilangan genap: "))
else:
    print("Benar!")