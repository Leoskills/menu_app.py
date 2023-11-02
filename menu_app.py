

def agregar_compra(lista_compras):
    monto_compra = float(input("Ingrese el monto de la compra: "))
    lista_compras.append(monto_compra)
    print("Compra agregada correctamente")

def mostrar_compras(lista_compras):

        print(lista_compras)



def sumar(lista_compras):
        suma = 0
        for elemento in lista_compras:
            suma += elemento
        print(f"Total gastado: ${suma}")


def menu():
    lista_compras =[]
    while True:
        print("MENU:")
        print("1. Agregar compra")
        print("2. Mostrar compra")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            agregar_compra(lista_compras)
        elif opcion == "2":
            mostrar_compras(lista_compras)
        elif opcion == "3":
            sumar(lista_compras)
        elif opcion == "4":
            print("¡Hasta luego!.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
menu()
