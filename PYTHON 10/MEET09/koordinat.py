print("<<< IDENTIFIKASI KUADRAN >>>")
x = int(input("Masukksn Nilai X: "))
y = int(input("MaSukksn Nilai Y: "))

if (x > 0) and (y > 0):
    print(f"Titik koordinat ({x},{y} pada Kuadran I)")
elif (x < 0) and (y > 0):
    print(f"Titik koordinat ({x},{y} pada Kuadran II)")
elif (x < 0) and (y < 0):
    print(f"Titik koordinat ({x},{y} pada Kuadran III)")
elif (x > 0) and (y < 0):
    print(f"Titik koordinat ({x},{y} pada Kuadran IV)")
elif (x == 0) and (y == 0):
    print(f"Titik koordinat ({x},{y} pada Titik Pusat)")