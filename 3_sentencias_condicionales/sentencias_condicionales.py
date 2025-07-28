while True:  # Bucle infinito
    # Solicitar al usuario que ingrese un número
    entrada = input("Introduce un número (o escribe 'salir' para terminar): ")

    if entrada.lower() == 'salir':  # Opción para salir del bucle
        print("¡Hasta luego!")
        break  # Salir del bucle

    try:
        number = float(entrada)  # Convertimos la entrada a un número flotante

        # Determinar si el número es positivo, negativo o cero
        if number > 0:
            print(f"El número {number} es positivo.")
        elif number < 0:
            print(f"El número {number} es negativo.")
        else:
            print("El número es cero.")
    except ValueError:
        print("Por favor, introduce un número válido.")
