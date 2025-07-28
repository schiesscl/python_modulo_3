# Función para convertir Celsius a Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir Fahrenheit a Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Menú de opciones
print("Conversor de Temperatura")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

# Solicitar al usuario que elija una opción
option = input("Elige una opción (1 o 2): ")

if option == '1':
    temp_celsius = float(input("Introduce la temperatura en Celsius: "))
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C es igual a {temp_fahrenheit}°F")
elif option == '2':
    temp_fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"{temp_fahrenheit}°F es igual a {temp_celsius}°C")
else:
    print("Opción no válida. Por favor, elige 1 o 2.")
    