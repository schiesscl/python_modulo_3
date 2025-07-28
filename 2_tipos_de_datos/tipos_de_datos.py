# Solicitar información del usuario
name = input("¿Cuál es tu nombre? ")  # Cadena
age = int(input("¿Cuántos años tienes? "))  # Entero
height = float(input("¿Cuál es tu altura en metros? "))  # Flotante
is_student_input = input("¿Eres estudiante? (Sí/No): ").strip()  # Entrada del usuario

# Verificar si la respuesta es afirmativa o negativa
is_student = is_student_input in ['sí', 'si', 's', 'yes', 'y', 'Sí', 'Si', 'S', 'Yes', 'Y']

# Verificar si la respuesta es negativa
no_answers = ['no', 'n', 'No', 'N']
is_not_student = is_student_input in no_answers

# Mostrar la información recopilada
print("\nInformación Recopilada:")
print(f"Nombre: {name}")
print(f"Edad: {age} años")
print(f"Altura: {height} metros")
print(f"¿Es estudiante?: {'Sí' if is_student else 'No' if is_not_student else 'Respuesta no válida'}")
