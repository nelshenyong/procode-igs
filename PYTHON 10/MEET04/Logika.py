# Operasi Logika di Python
# 1. and
# 2. or
# 3. xor '^'
# 4. not

print('- AND -')
print("True - True")
a = True
b = True
hasil = a and b
print(a, 'and', b, '=', hasil)

print("True - False")
a = True
b = False
hasil = a and b
print(a, 'and', b, '=', hasil)

print("False - True")
a = False
b = True
hasil = a and b
print(a, 'and', b, '=', hasil)

print("False - False")
a = False
b = False
hasil = a and b
print(a, 'and', b, '=', hasil)
print(" ")




print('- OR -')
print("True - True")
a = True
b = True
hasil = a or b
print(a, 'or', b, '=', hasil)

print("True - False")
a = True
b = False
hasil = a or b
print(a, 'or', b, '=', hasil)

print("False - True")
a = False
b = True
hasil = a or b
print(a, 'or', b, '=', hasil)

print("False - False")
a = False
b = False
hasil = a or b
print(a, 'or', b, '=', hasil)
print(" ")




print('- XOR -')
print("True - True")
a = True
b = True
hasil = a ^ b
print(a, '^', b, '=', hasil)

print("True - False")
a = True
b = False
hasil = a ^ b
print(a, '^', b, '=', hasil)

print("False - True")
a = False
b = True
hasil = a ^ b
print(a, '^', b, '=', hasil)

print("False - False")
a = False
b = False
hasil = a ^ b
print(a, '^', b, '=', hasil)
print(" ")




print('- NOT -')
print("Not A")
a = False
b = True
hasil = not a
print('not', a, '=', hasil)
print("Not B")
hasil = not b
print('not', b, '=', hasil)