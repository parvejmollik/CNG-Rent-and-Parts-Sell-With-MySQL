import inventory, sales

while True:
    print("\n1. Add Product\n2. List Products\n3. Record Sale\n4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        inventory.add_product(name, price, stock)
    elif choice == '2':
        inventory.list_products()
    elif choice == '3':
        pid = int(input("Product ID: "))
        qty = int(input("Quantity: "))
        sales.record_sale(pid, qty)
    elif choice == '4':
        break
