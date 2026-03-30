from almacen import add_product, calculate_statistics, export_csv, import_csv 
# Imports functions from the almacen module for correct program execution

import csv
# Imports CSV configurations

warehouse = []  # List that will store dictionaries to serve as the inventory

def menu():
    """
    This function is responsible for printing the available menu options to the console
    """
    print("=" * 30)
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Upload CSV")
    print("9. Exit")
    print("=" * 30)

def loop():
    """
    The loop() function is the engine of the program
    menu() displays the options
    options() captures and executes the user's choice and returns the selected number
    The while loop keeps running until that number is 9
    """
    
    loop_var = 0
    while loop_var != 9:
        menu()
        loop_var = options()

def options():
    valid_option = False
    while not valid_option:
        try:
            option = int(input(">> Select an option: "))
            if 1 <= option <= 9:
                valid_option = True
            else:
                print("\nInvalid selection, enter a value between 1 and 9.")
        except ValueError:
            print("\nInvalid input. Please enter numbers only.")

    if option == 1:
        product = add_product()
        warehouse.append(product)

    elif option == 2:
        for pdt in warehouse:
            print("| Name:", pdt["Name"], "| Quantity:", pdt["Stock"], "| Unit Price: $", pdt["Unit_price"], "|")

    elif option == 3:
        search = input("| Enter the product name to search: \n").capitalize().strip()
        found = False                      
        for pdt in warehouse:
            if pdt["Name"] == search:
                found = True
                print("| Name:", pdt["Name"], "| Quantity:", pdt["Stock"], "| Unit Price: $", pdt["Unit_price"], "|")
                break
        if not found:                      
            print("| Product not found in inventory\n")

    elif option == 4:
        search = input("| Enter the product name to update: ").capitalize().strip()
        found = False
        for pdt in warehouse:
            if pdt["Name"] == search:
                found = True
                print("What do you want to update?")
                print("1. Name")
                print("2. Stock")
                print("3. Unit Price")

                valid_sub = False
                while not valid_sub:
                    try:
                        update_option = int(input("Select an option: "))
                        if 1 <= update_option <= 3:
                            valid_sub = True
                        else:
                            print("Invalid option, enter 1, 2 or 3.")
                    except ValueError:
                        print("Invalid input. Enter a number.")

                if update_option == 1:
                    new_name = input("New name: ").capitalize().strip()
                    pdt["Name"] = new_name
                elif update_option == 2:
                    new_stock = int(input("New stock: "))
                    pdt["Stock"] = new_stock
                elif update_option == 3:
                    new_price = float(input("New price: "))
                    pdt["Unit_price"] = new_price

                print("Product updated successfully")
                break

        if not found:
            print("Product not found")

    elif option == 5:
        search = input("Product to delete: ").capitalize().strip()
        found = False
        for pdt in warehouse:
            if pdt["Name"] == search:
                warehouse.remove(pdt)
                print("Product deleted")
                found = True
                break
        if not found:
            print("Product not found")

    elif option == 6:
        calculate_statistics(warehouse)

    elif option == 7:
        export_csv(warehouse)

    elif option == 8:
        import_csv(warehouse)

    elif option == 9:
        print("Exiting the system")
        exit()

loop()
