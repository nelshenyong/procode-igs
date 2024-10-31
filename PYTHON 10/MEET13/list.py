#List dengan angka
list_num = [1,24,2,25,22,23,]
print(f"Data list num: {list_num}")

print("-"*27)
list_str = ["a", "b", "c"]
print(f"Data list string: {list_str}")

print("-"*27)
list_bool =  [True, False, True, False]
print(f"Data list boolean: {list_bool}")

print("-"*27)
list_campur =  [1,2,3,4,"a","b","c","d", True, False]
print(f"Data list campur: {list_campur}")

print("-"*27)
data_range = list(range(1,11))
print(f"Value data range: {data_range}")

print("-"*27)
data_list_for = [i for i in range (1,16,2)]
# range(start, stop, step)
print(f"Value data range: {data_list_for}")

print("-"*27)
data_list_for_if = [i for i in range(20,31) if i != 25]
print(f"Value data for if: {data_list_for_if}")

print("-"*27)
data_list_for_if2 = [z for z in range(30,46) if z % 2 == 0]
print(f"Value data for if (Genap): {data_list_for_if2}")

print("-"*27)
data_list_for_if3 = [z for z in range(30,46) if z % 2 == 1]
print(f"Value data for if (Ganjil): {data_list_for_if3}")

print("-"*27)
data_list_for_if4 = [z for z in range(30,46) if z % 2 == 1 and z !=33]
print(f"Value data for if (Ganjil) z! = 33: {data_list_for_if4}")