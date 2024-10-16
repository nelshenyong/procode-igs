print("Program Temperatur - Kelvin")

kelvin = float(input("Masukan suhu: "))

celsius = kelvin - 273.15
fahrenheit = ((9 / 5)* (kelvin - 273.15)) + 32
reaumure = (4 / 5)* (kelvin - 273.15)

print("CELSIUS: ", celsius)
print("FAHRENHEIT: ", fahrenheit)
print("REAUMURE: ", reaumure)