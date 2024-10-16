datals_1 = ["a", "b", "c"]
datals_2 = ["s", "m", "a"]
list_normal = datals_1 + datals_2
print(f"list normal: {list_normal}")

list_nested = [datals_1, "x", "x", "y", datals_2]
print(f"list nested: {list_nested}")
print(f"Data 0 pada list nested: {list_nested[0][0]}")
print(f"Data -1,-2 pada list nested: {list_nested[-1][-2]}")
list_nested_copy = list_nested.copy()

print(f"List nested: {list_nested}")
print(f"List nested copy: {list_nested_copy}")
list_nested_copy[0][0] = "awal"
print(f"List nested diupdate: {list_nested}")
print(f"List nested copy diupdate: {list_nested_copy}")

print(f"Addres memory: {hex(id(list_nested))}")
print(f"Addres memory: {hex(id(list_nested_copy))}")

print("\n", "-"*35)
from copy import deepcopy

data1 = ["i", "g", "S"]
data2 = [1,2,3,4]
data12 = [data1,data2]
print(f"data 12: {data12}")
data12_copy = deepcopy(data12)
print(f"data 12 copy{data12_copy}")
data12_copy[0][0]="igs"

print(f"data 12 copy diupdate: {data12_copy}")
