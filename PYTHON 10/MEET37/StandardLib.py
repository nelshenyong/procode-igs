import os
import platform

if(platform.system()=='Linux'):
    os.system("clear")
elif (platform.system()=='Windows'):
    os.system("cls")
    
import math

x = 6
print(f"Faktorial dari (! {x}) = {math.factorial(x)} ")
data = [2,3,3]
#fsum
print(f"Hasil tambah = {math.fsum(data)}")

print(f"Hasildari pembulatan ceil 5.57 adalah {math.ceil(5.57)}")