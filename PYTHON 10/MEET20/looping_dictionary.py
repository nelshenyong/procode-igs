data_kota = {
    "plg" : "Palembang",
    "jkt" : "Jakarta",
    "sby" : "Surabaya",
    "bdg" : "Bandung"
}

#1
for i in data_kota:
    print(i)



#2
data_key = data_kota.keys()
print(data_key)

for key in data_key:
    print(f"{data_kota.get(key)}")


print("_"*25)
#3
data_value = data_kota.values()
for k in data_value:
    print(k)


print("_"*25)
#4
data_item = data_kota.items()
for key,value in data_item:
    print(f"Key: {key} | Value: {value}")






























































































