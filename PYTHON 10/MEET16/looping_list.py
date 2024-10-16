print("<<\t List dengan perulangan for: ")

data_list1 = [1, 34, 314, 413, 34, 1422113, 134314, 123, 134, 124]
for i in data_list1:
    print(f"Data list 1: {i}")

print("<<\tList dengan perulangan for, range: ") 
data_list1_panjang = len(data_list1)
for i in range(data_list1_panjang):
    print(f"Data list 1:{i}")

print("<<\tList dengan perulangan while: ")
list2 = ["i", "g", "s", 1] 

i = 0
list2_panjang = len(list2)
while i < list2_panjang:
    print(f"List 2: {list2[i]}")
    i += 1

print("<<\tList dengan comprehension: ")
[print(f"List adalah: {i}") for i in list2]

print("<<\tList dengan kuadrat: ")
list3 = [2, 6, 3, 4, 5]
[print(f"List 3 dikuadratkan: {i**2}") for i in list3]

print("<<\tList dengan enumerate: ")
for index, data in enumerate(list3):
    print(f"Index: {index+1}, {data}")

print("<<\tList dengan enumerate: ")
list4 = []
list4.append("Budi")
list4.append("Budu")
list4.append("Bunga")
print(list4)

