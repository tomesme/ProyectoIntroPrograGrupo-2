print('Hola mundo')

accion = 0

while accion != 2:
    print("Menu:")
    print("1. Ingresar nueva compra ")
    print("2. Salir ")
    
    accion = int(input("Seleccione una acción: "))

    if accion == 1:
        compra = int(input("Ingresar una nueva compra: "))
    elif accion == 2:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente de nuevo.2")
    