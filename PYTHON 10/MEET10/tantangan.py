while True:
    try:
        bilangan = int(input("Masukkan bilangan: "))
        if (10 <= bilangan <= 15) or (20 <= bilangan <= 25) or (35 <= bilangan <= 40):
            print("Benar")
        else:
            print("Salah")
    except ValueError:
        print("Input harus bilangan bulat.")