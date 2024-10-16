usernamekey = "orang"
Passwordkey = "igs"

i = 0 
while i != 3:
    i += 1

    username = input("Masukan username: ")
    password = input("Masukan password: ")
   
    if (usernamekey == username) and (Passwordkey == password):
        print("Login berhasil....")
        break

    elif (usernamekey == password) or (Passwordkey == password):
        print("username atau password salah ! ")

else:
    print("Gagal login sudah 3x")