print("Program Temperatur - Fahrenheit")

fahrenheit = float(input("Masukan suhu: "))

celsius = (5 / 9)* (fahrenheit - 32)
kelvin = ((5 / 9)* (fahrenheit - 32)) + 273.15
reaumure = (4 / 9)* (fahrenheit - 32)

print("CELSIUS: ", celsius)
print("KELVIN: ", kelvin) 
print("REAUMURE: ", reaumure)