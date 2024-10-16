data_1 = ["i", "g", "s"]
data_2 = data_1

print(f"Data 1: {data_1}")
print(f"Data 2: {data_2}")

data_1[0] = "z"
print(f"Data 1 update: {data_1}")
print(f"Data 2 update: {data_2}")

print(f"Addres memory data 1: {hex(id(data_1))}")
print(f"Addres memory data 2: {hex(id(data_2))}")

print("-"*35)
data_3 = ["x", "y", "z"]
data_4 = data_3.copy()

print(f"Data 3: {data_3}")
print(f"Data 4: {data_4}")

data_3[1] = "abc"
print(f"Data 3 update: {data_3}")
print(f"Data 4 update: {data_4}")

print(f"Addres memory data 3: {hex(id(data_3))}")
print(f"Addres memory data 4: {hex(id(data_4))}")