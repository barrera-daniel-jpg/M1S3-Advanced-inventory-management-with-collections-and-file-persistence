from almacen import add_product, calcular_estadisticas, exportar_csv, importar_csv 
# Importa las fucniones del modulo almacen para la correcta ejecucion del programa
import csv
# Importa las configuracions del csv

bodega = [] #Lista que va almacenar diccionarios con el fin de que sriva como el inventario.

def menu():
    """
    
    Esta funcion es la encarga de imprimir en consola las opcines del menu disponibles para el usuario
    
    """
    print("="*30)
    print("1.Add")
    print("2.View")
    print("3.Search")
    print("4.Refresh")
    print("5.Delete")
    print("6.Statistics")
    print("7.Save CSV")
    print("8.Upload CSV")
    print("9.Exit")
    print("="*30)

def loop():
    """
    La funcion loop() es el motor del programa
    menu() muestra las opciones
    options() captura y ejecuta la opción del usuario y retorna el número elegido
    El while sigue girando hasta que ese número sea 9
    
    """
    
    loop_var = 0
    while loop_var != 9:
        menu()
        loop_var = options()

def options():
    opcion_valida = False
    while not opcion_valida:
        try:
            option = int(input(">> Seleccione una opcion: "))
            if 1 <= option <= 9:
                opcion_valida = True
            else:
                print("\nSeleccion invalida, ingrese un valor entre 1 y 9.")
        except ValueError:
            print("\nEntrada invalida. Por favor ingrese solo numeros.")

    if option == 1:
        product = add_product()
        bodega.append(product)

    elif option == 2:
        for pdt in bodega:
            print("| Nombre:", pdt["Name"], "| Cantidad:", pdt["Stock"], "| Precio Unitario: $", pdt["Unit_price"], "|")

    elif option == 3:
        buscar = input("Ingrese nombre del producto que desea buscar: ").capitalize().strip()
        encontrado = False                      
        for pdt in bodega:
            if pdt["Name"] == buscar:
                encontrado = True
                print("| Nombre:", pdt["Name"], "| Cantidad:", pdt["Stock"], "| Precio Unitario: $", pdt["Unit_price"], "|")
                break
        if not encontrado:                      
            print("El producto no se encuentra en el inventario")

    elif option == 4:
        buscar = input("Ingrese el nombre del producto a actualizar: ").capitalize().strip()
        encontrado = False
        for pdt in bodega:
            if pdt["Name"] == buscar:
                encontrado = True
                print("¿Qué desea actualizar?")
                print("1. Nombre")
                print("2. Stock")
                print("3. Precio Unitario")

                
                sub_valida = False
                while not sub_valida:
                    try:
                        opcion_update = int(input("Seleccione una opción: "))
                        if 1 <= opcion_update <= 3:
                            sub_valida = True
                        else:
                            print("Opción invalida, ingrese 1, 2 o 3.")
                    except ValueError:
                        print("Entrada invalida. Ingrese un número.")

                if opcion_update == 1:
                    nuevo_nombre = input("Nuevo nombre: ").capitalize().strip()
                    pdt["Name"] = nuevo_nombre
                elif opcion_update == 2:
                    nuevo_stock = int(input("Nuevo stock: "))
                    pdt["Stock"] = nuevo_stock
                elif opcion_update == 3:
                    nuevo_precio = float(input("Nuevo precio: "))
                    pdt["Unit_price"] = nuevo_precio

                print("Producto actualizado correctamente")
                break

        if not encontrado:
            print("Producto no encontrado")

    elif option == 5:
        buscar = input("Producto a eliminar: ").capitalize().strip()
        encontrado = False
        for pdt in bodega:
            if pdt["Name"] == buscar:
                bodega.remove(pdt)
                print("Producto eliminado")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado")

    elif option == 6:
        calcular_estadisticas(bodega)

    elif option == 7:
        exportar_csv(bodega)

    elif option == 8:
        importar_csv(bodega)

    elif option == 9:
        print("Saliendo del sistema")
        exit()

    

loop()
