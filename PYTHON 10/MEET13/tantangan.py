data_list = [z for z in range(1,100) if z % 2 == 0 and 10 <= z <= 20 or z % 2 == 0 and 90 <= z <= 100]
print(f"{data_list}")