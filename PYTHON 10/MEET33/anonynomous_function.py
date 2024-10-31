#list - filter data: 
#sintak : list(filter(kondisi,  data))

def batas():
    print("-"*25)
    
data = [2,3,4,5,6,8,10,1]

#dengan def:
def kurang5(x):
    return x < 6

hasil_def = list(filter(kurang5, data))
print(sorted(hasil_def))
batas()

#Jika dengan lambda 
hasil_lambda = list(filter(lambda x : x < 6, data))
print(sorted(hasil_lambda))

batas()
#ganjil & genap
ganjil = list(filter(lambda x : x % 2 == 1, data))
print(f"Ganjil = {sorted(ganjil)}")

genap = list(filter(lambda x : x % 2 == 0, data))
print(f"Genap = {sorted(genap)}")

#jika, dengan list - loops
hasil_list = [x for x in data if x % 2 == 0]
print(f"List loop = {sorted(hasil_list)}")

batas()
#list - > func map
#sintak : list(map(kondisi, data))

hasil_lambda = list(map(lambda x : x*2, data))
print(f"Hasil map = {sorted(hasil_lambda)}")

hasil_list_for2 =[x*2 for x in data]
print(f"Map with loops = {sorted(hasil_list_for2)}")

#Anymous function = fungsi yang tidak terdefinisi,
# Akan berguna : fungsi yang memiliki argument dapat di pecah ke banyak fungsi: disebut (carrying)
batas()
def pangkat(x):
    return lambda y : y ** x
pangkat3 = pangkat(2)
print(pangkat3(2))

pangkat4 = pangkat(4)
print(pangkat4(3))

