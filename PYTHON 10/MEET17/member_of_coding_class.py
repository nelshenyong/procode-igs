i=0
member = []
while i < 40 :
    nama = input("Masukan Nama Member \t\t: ")
    kelas = input("Masukan Kelas Member \t\t: ")
    jk = input("Masukan Jenis Kelamin Member (L/P)\t: ")
    tambah_member = [nama,kelas,jk]
    member.append(tambah_member)
    i+=1
    for index,data in enumerate(member):
        print(f"{index+1} | {data[0]} | {data[1]} | {data[2]}")
    if i >= 10 :
        status = input("apakah ingin lanjut? (Y/N) : ").upper()
        if status == "Y" :
            continue
        else :
            break

