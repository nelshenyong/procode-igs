import numpy as npy

data_list = [2,4,5,7]
print(f"data list = {data_list}")

data_matrik_a = npy.array(data_list)
print(f"data matrik = {data_matrik_a}")

data_matrik_a_x2 = data_matrik_a * 2
print(f"data_matik_a_x2 = {data_matrik_a_x2}")

print(f"data_list_x2 = {data_list*2}")

print(f"pangkat 2 matrik = {data_matrik_a **2}")
# print(f"pangkat 2 list = {data_list **2}") tidak bisa

print("*" *30)

matrik_b = npy.array([(2,5,6,8), (6,3,1,10), (2,3,4,1)])
print(f"matrik b = \n{matrik_b}")

matrik_c = npy.array([[2], [4], [6]])
print(f"matrik c = \n{matrik_c}")

print(f"matrik b + matrik c = {matrik_b + matrik_c}")
print(f"matrik b + matrik c = {matrik_b - matrik_c}")
print(f"matrik b + matrik c = {matrik_b * matrik_c}")
print(f"matrik b + matrik c = {matrik_b / matrik_c}")

