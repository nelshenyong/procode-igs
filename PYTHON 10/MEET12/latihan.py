#cara manual
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

print("-"*27)
#cara for : membuat segitiga
for i in range(10) :
    print("*"*i)

print("-"*27)
#cara while : membuat segitiga
i = 0
while i < 10 :
    i+=1
    print("*"*i)

print("-"*27)
#cara while : dengan control statement membuat segitiga
for i in range(100):
    print("*"*i)

    if i == 10 : break

print("-"*27)
#cara while : dengan control statement membuat segitiga
i=0
while True :
    print("*"*i)
    i += 1
    if i == 12 : break

#while, untuk membuat segitiga tampil ganjil ganjil saja, control statement
print("-"*27)
i=0

while True :
    i += 1

    if i == 20 :
        break
    elif i%2:
        print("*"*i)
    else : continue
#membuat segitiga sama sisi, while control statement
i = 0
count = 20
spasi = int(20/2)
while True :
    i += 1
    if i == count :
        break
    elif i % 2 :
        print(" "*spasi,"*"*i)
        spasi -= 1

#membuat segitiga sama sisi terbalik, while control statement
print("-"*27) 
i = 20
count = 0
spasi = int(20/2)
while True :
    i -= 1
    if i == count :
        break
    elif i % 2 :
        print(" "*spasi,"*"*i)
        spasi += 1