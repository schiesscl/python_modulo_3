def area_circle(radius):
    """
    Calcula el área de un círculo dado su radio.
    
    Parámetro:
    radius (float): El radio del círculo.
    
    Retorna:
    float: El área del círculo.
    """
    return 3.14159 * (radius ** 2)  # Fórmula del área: π * r^2

def area_rectangle(length, width):
    """
    Calcula el área de un rectángulo dado su largo y ancho.
    
    Parámetros:
    length (float): El largo del rectángulo.
    width (float): El ancho del rectángulo.
    
    Retorna:
    float: El área del rectángulo.
    """
    return length * width  # Fórmula del área: largo * ancho

def area_triangle(base, height):
    """
    Calcula el área de un triángulo dado su base y altura.
    
    Parámetros:
    base (float): La base del triángulo.
    height (float): La altura del triángulo.
    
    Retorna:
    float: El área del triángulo.
    """
    return (base * height) / 2  # Fórmula del área: (base * altura) / 2

def main():
    print("Cálculo de áreas de figuras geométricas")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    
    option = input("Elige una opción (1, 2 o 3): ")
    
    if option == '1':
        radius = float(input("Introduce el radio del círculo: "))
        area = area_circle(radius)
        print(f"El área del círculo es: {area:.2f}")
    elif option == '2':
        length = float(input("Introduce el largo del rectángulo: "))
        width = float(input("Introduce el ancho del rectángulo: "))
        area = area_rectangle(length, width)
        print(f"El área del rectángulo es: {area:.2f}")
    elif option == '3':
        base = float(input("Introduce la base del triángulo: "))
        height = float(input("Introduce la altura del triángulo: "))
        area = area_triangle(base, height)
        print(f"El área del triángulo es: {area:.2f}")
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
