# Inicializamos la agenda como un diccionario vacío
agenda = {}

def add_contact(name, phone, email):
    """
    Función para agregar un contacto a la agenda.
    
    Parámetros:
    name (str): El nombre del contacto.
    phone (str): El número de teléfono del contacto.
    email (str): El correo electrónico del contacto.
    """
    # Almacenamos el contacto en el diccionario 'agenda'
    agenda[name] = {
        'phone': phone,  # Guardamos el teléfono del contacto
        'email': email   # Guardamos el email del contacto
    }
    # Mensaje de confirmación al agregar el contacto
    print(f"Contacto {name} agregado exitosamente.")

def show_contacts():
    """
    Función para mostrar todos los contactos en la agenda.
    """
    # Verificamos si la agenda está vacía
    if not agenda:
        print("La agenda está vacía.")  # Mensaje si no hay contactos
    else:
        print("\nLista de Contactos:")  # Encabezado para la lista de contactos
        # Recorremos el diccionario 'agenda' para mostrar cada contacto
        for name, details in agenda.items():
            # Imprimimos el nombre, teléfono y email de cada contacto
            print(f"Nombre: {name}, Teléfono: {details['phone']}, Email: {details['email']}")

def delete_contact(name):
    """
    Función para eliminar un contacto de la agenda.
    
    Parámetro:
    name (str): El nombre del contacto a eliminar.
    """
    # Verificamos si el contacto existe en la agenda
    if name in agenda:
        del agenda[name]  # Eliminamos el contacto del diccionario
        print(f"Contacto {name} eliminado exitosamente.")
    else:
        print(f"El contacto {name} no se encuentra en la agenda.")

while True:  # Bucle principal que permite al usuario interactuar con el programa
    print("\nMenú:")  # Encabezado del menú
    print("1. Agregar contacto")  # Opción para agregar un nuevo contacto
    print("2. Mostrar contactos")  # Opción para mostrar todos los contactos
    print("3. Eliminar contacto")  # Opción para eliminar un contacto
    print("4. Salir")  # Opción para salir del programa
    
    option = input("Elige una opción (1, 2, 3 o 4): ")  # Solicitar al usuario que elija una opción

    # Condicional para manejar la opción elegida por el usuario
    if option == '1':
        # Solicitar al usuario que ingrese los detalles del contacto
        contact_name = input("Introduce el nombre del contacto: ")
        contact_phone = input("Introduce el teléfono del contacto: ")
        contact_email = input("Introduce el email del contacto: ")
        # Llamar a la función para agregar el contacto
        add_contact(contact_name, contact_phone, contact_email)
    elif option == '2':
        # Llamar a la función para mostrar los contactos
        show_contacts()
    elif option == '3':
        # Solicitar al usuario que ingrese el nombre del contacto a eliminar
        contact_name_to_delete = input("Introduce el nombre del contacto a eliminar: ")
        # Llamar a la función para eliminar el contacto
        delete_contact(contact_name_to_delete)
    elif option == '4':
        print("¡Hasta luego!")  # Mensaje de despedida
        break  # Salir del bucle y terminar el programa
    else:
        print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")  # Mensaje si la opción no es válida