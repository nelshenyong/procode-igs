i=0
member = []
while i < 40 :
    nama = input("Nama buku \t: ")
    penulis = input("Nama penulis \t: ")
    terbit = input("Tahun terbit \t: ")
    tambah = [nama, penulis, terbit]
    print("-"*10)
    print(f"Jumlah buku: {len(member)}")
    member.append(tambah)
    i+=1
    print(f"{nama} | {penulis} | {terbit}")
    print("-"*27)
    if i >= 3:
        status = input("Apakah ingin lanjut? (Y/N): ").upper()
        if status == "Y" :
            continue
        if status == "N":  
             print("<<< DAFTAR BUKU >>>")
             for index,data in enumerate(member):
                 print(f"{index+1} | {data[0]} | {data[1]} | {data[2]}")
                 print("-"*27)
             break
        else:
            print("-"*77)
            print("Tidak sesuai pilihan!")
            break