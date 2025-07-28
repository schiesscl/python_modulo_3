def multiplication_table():
    number = int(input("Introduce un número para generar su tabla de multiplicar: "))
    print(f"\nTabla de multiplicar del {number}:")
    for i in range(1, 20):  # Genera la tabla del 1 al 10
        print(f"{number} x {i} = {number * i}")

def calculate_factorial():
    number = int(input("Introduce un número para calcular su factorial: "))
    factorial = 1
    for i in range(1, number + 1):  # Calcula el factorial
        factorial *= i
    print(f"El factorial de {number} es {factorial}")

while True:  # Bucle principal
    print("\nMenú:")
    print("1. Generar tabla de multiplicar")
    print("2. Calcular factorial")
    print("3. Salir")
    
    option = input("Elige una opción (1, 2 o 3): ")

    if option == '1':
        multiplication_table()
    elif option == '2':
        calculate_factorial()
    elif option == '3':
        print("¡Hasta luego!")
        break  # Salir del bucle
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
