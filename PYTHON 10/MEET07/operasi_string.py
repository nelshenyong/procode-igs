# Menghitung banyak data str
data = "IGNATIUS GLOBAL SCHOOL"
print(f"Jumlah str pada data adalah: {len(data)}")

# in - not in
print(f"Apakah ada str 'Z' dalam data: {('Z' in data)}")
print(f"Apakah ada str 'Z' dalam data: {('Z' not in data)}")

# Menghitung karangter str dalam data
print(f"Jumlah str o data: {data.count('O')}")

#Indexing data
print(f"Data ke-0 adalah: {data[0]}")
print(f"Data ke-3 adalah: {data[3]}")
print(f"Data ke-0_5 adalah: {data[0:5]}")

# Contoh beberapa metode yang ada di str
print(f"Data akan menjadi Upper case: {data.upper()}")
print(f"Data akan menjadi Lower case: {data.lower()}")

# \n (New Line)
# \t (Tab)
print(f"IGNATIUS \n GLOBAL \n SCHOOL")
print(f"IGNATIUS \t GLOBAL \t SCHOOL")