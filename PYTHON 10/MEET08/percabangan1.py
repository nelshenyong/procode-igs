print("Hitungan Nilai Percabangan Sekolah")

pts = int(input("Masukkan Nilai Tengah Semester: "))
pas = int(input("Masukkan Nilai Akhir Semester: "))

akhir = (0.4 * pts) + (0.6 * pas)
print(f"Nilai Akhir: ", akhir)

if akhir == 100 :
    print(f">> SEMPURNA <<")