import csv

def add_product():
    """
   1) Valid = 0 / while valid != 1 garantiza que el usuario ingrese un valor válido antes de continuar
   
    """
    
    valid = 0
    while valid != 1:
        name = str(input("\n| Ingrese el nombre del producto: ")).capitalize().strip()
        if name == "":
            print("El nombre no puede estar vacío")
        else:
            valid = 1

    valid = 0
    while valid != 1:
        try:
            stock = int(input("| Ingrese el stock: "))
            if stock < 0:
                print("\nEl stock no puede ser negativo")
            else:
                valid = 1
        except ValueError:
            print(">> Error <<: El stock debe ser un número entero")

  
    valid = 0
    while valid != 1:
        try:
            unit_price = float(input("| Ingrese el precio unitario: $ "))
            if unit_price < 0:
                print("El precio no puede ser negativo")
            else:
                valid = 1
        except ValueError:
            print("Error: El precio debe ser un número")
    
   
    product_and_more = {"Name": name, "Stock": stock, "Unit_price": unit_price} 
    print(f"El producto registrado satisfactoriamente")
    return product_and_more 
    # La variable product_and_more retorna el diccionario con los datos del producto para usarlo fuera




def calcular_estadisticas(inventario):
    """
    1) if not inventario valida si la lista esta vacia antes de calcular
    2) 
    """
    # Si el inventario esta vacion imprime esto:
    if not inventario:
        print("El inventario está vacío.")
        return
 
    subtotal = lambda p: p["Unit_price"] * p["Stock"]   # Lambda para calcular el subtotal de cada producto
    unidades_totales = sum(p["Stock"] for p in inventario) 
    # Suma la cantidad de productos y los cuantifica para validar la cantidad de articulos que hay en el invetario
    valor_total = sum(subtotal(p) for p in inventario) 
    # Suma todo los subtotales de los prodcuto y da el valor neto total de toda la mercancia
    producto_mas_caro = max(inventario, key=lambda p: p["Unit_price"]) # Recorre el inventario y encuentra el producto mas caro
    producto_mayor_stock = max(inventario, key=lambda p: p["Stock"]) # Recorre el inventario y encuentra el producto con mayor precio
  
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DEL INVENTARIO")
    print("=" * 40)
    print(f"Unidades totales en stock : {unidades_totales}") # Imprime en consola las unidades totales
    print(f"Valor total del inventario : ${valor_total:,.2f}") # Imprime en consola el valor total del inventario
    print(f"Producto más caro : {producto_mas_caro['Name']} (${producto_mas_caro['Unit_price']:,.2f})") # Imprime en consola el producto mas caro
    print(f"Mayor stock : {producto_mayor_stock['Name']} ({producto_mayor_stock['Stock']} unidades)")# Imprime en consola con mayor stock
    print("-" * 40)
    print("  Subtotales por producto:")
    for p in inventario:
        print(f"  >> {p['Name']} = ${subtotal(p):,.2f} ") # Imprime en consola el subtotal de cada producto
    print("=" * 40 + "\n")

def exportar_csv(bodega):
    """
    1) exportar_csv es la funcion encarga de exportar la lista bodega la cual contiene los diccionarios
        con los productos y sus caracteristicas
    """
    
    with open("bodega.csv", "w", newline="", encoding="utf-8") as archivo:
        # Crea el archivo para escribir, y lo cierra automáticamente al terminar
        campos = ["Name", "Stock", "Unit_price"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        #  escribe archivos CSV a partir de diccionarios
        # haciendo coincidir las claves del diccionario con los encabezados de columna definidos
        
        escritor.writeheader()        # Escribe la fila de encabezados: Name, Stock, Unit_price
        escritor.writerows(bodega)    # Escribe todos los productos
    print("Inventario guardado en bodega.csv")


def importar_csv(bodega):

    try:
        with open("bodega.csv", "r", newline="", encoding="utf-8") as archivo: 
        # Abre el archivo para escribir, y lo cierra automáticamente al terminar
            
            lector = csv.DictReader(archivo)
            bodega.clear() # Limpia la lista actual
            for fila in lector:
                bodega.append({
                    "Name": fila["Name"],
                    "Stock": int(fila["Stock"]), # CSV guarda todo como texto
                    "Unit_price": float(fila["Unit_price"]) # hay que convertir
                    # csv guarda todo como texto y hay que convertir a int y float
                })
        print(f"Inventario cargado: {len(bodega)} productos.") # Imprime en consola la cantidad de productos del archivo
    except FileNotFoundError:
        print("No se encontró el archivo bodega.csv") # Evalua si no hay un archivo en la carpeta
