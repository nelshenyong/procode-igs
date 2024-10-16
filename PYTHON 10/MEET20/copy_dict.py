data_kota = {
    "plg" : "Palembang",
    "jkt" : "Jakarta",
    "sby" : "Surabaya",
    "bdg" : "Bandung"
}

data_kota_copy = data_kota
print(f"Data kota ori: {data_kota}")
print(f"Data kota copy: {data_kota_copy}")

data_kota['plg'] = "PALEMBANG WONG KITO"
print(f"Data kota ori update: {data_kota}")
print(f"Data kota copy update: {data_kota_copy}")

print("-"*25, "\n")

data_sekolah = {
    "sma" : "SMA IGNATIUS GLOBAL SCHOOL",
    "smp" : "SMP IGNATIUS GLOBAL SCHOOL",
    "sd" : "SD IGNATIUS GLOBAL SCHOOL"
}

data_sekolah_copy = data_sekolah.copy()
data_sekolah["sma"] = "SMA IGS KEREN"
print(f"Data sekolah : {data_sekolah}")
print(f"Data sekolah copy : {data_sekolah_copy}")


print("*"*30, "\n")
data1 = data_sekolah.pop("sma")
print(f"Data sekolah terbaru: {data_sekolah}")
print(data1)

print("*"*30, "\n")
data2 = data_sekolah.popitem()
print(f"Data sekolah terbaru 2: {data_sekolah}")
print(data2)