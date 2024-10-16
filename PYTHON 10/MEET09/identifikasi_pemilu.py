print ("<<< IDENTIFIKASI PEMILU >>>")
umur = int(input("Mausukkan Umur Anda: "))

if umur >= 17:
    print("Anda boleh ikut pemilu!")
elif umur < 17:
    status = input("Status Menikah (Y/N)").upper()
    if status == "Y":
         print("Anda boleh ikut pemilu!")
    if status == "N":
         print("Anda tidak boleh ikut pemilu!")
    else:
         print("Salah input status menikah!")
else:
     print("Salah input umur!")