from collections import Counter

def add_product():
    
    valid = 0
    while valid != 1:
        name = str(input("Ingrese el nombre del producto: ")).capitalize().strip()
        if name == "":
            print("El nombre no puede estar vacío")
        else:
            valid = 1

    
    valid = 0
    while valid != 1:
        try:
            stock = int(input("Ingrese el stock: "))
            if stock < 0:
                print("El stock no puede ser negativo")
            else:
                valid = 1
        except ValueError:
            print("Error: El stock debe ser un número entero")

  
    valid = 0
    while valid != 1:
        try:
            unit_price = float(input("Ingrese el precio unitario: "))
            if unit_price < 0:
                print("El precio no puede ser negativo")
            else:
                valid = 1
        except ValueError:
            print("Error: El precio debe ser un número")

    product_and_more = {"Name": name, "Stock": stock, "Unit_price": unit_price}
    print(f"El producto registrado satisfactoriamente")
    return product_and_more

def calcular_estadisticas(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    # Lambda para calcular el subtotal de cada producto
    subtotal = lambda p: p["Unit_price"] * p["Stock"]

    unidades_totales = sum(p["Stock"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["Unit_price"])
    producto_mayor_stock = max(inventario, key=lambda p: p["Stock"])

    print("\n" + "=" * 40)
    print("       ESTADÍSTICAS DEL INVENTARIO")
    print("=" * 40)
    print(f"   Unidades totales en stock : {unidades_totales}")
    print(f"   Valor total del inventario: ${valor_total:,.2f}")
    print(f"   Producto más caro         : {producto_mas_caro['Name']} (${producto_mas_caro['Unit_price']:,.2f})")
    print(f"   Mayor stock               : {producto_mayor_stock['Name']} ({producto_mayor_stock['Stock']} unidades)")
    print("-" * 40)
    print("  Subtotales por producto:")
    for p in inventario:
        print(f"    - {p['Name']:<15} ${subtotal(p):>10,.2f}")
    print("=" * 40 + "\n")
