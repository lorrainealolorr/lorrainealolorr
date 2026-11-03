# Food Ordering System

menu = {
    1: ("Fried chicken", 35),
    2: ("Watermelon", 40),
    3: ("Kool aid", 15),
    4: ("Grapes", 15),
    5: ("Siomai", 30),
    6: ("Bottled Water", 15),
    7: ("Rice", 15)
}

cart = []
orders = []


def show_menu():
    print("\n--- MENU ---")
    print("================================")
    print(" No.   Food               Price")
    print("================================")

    for number, food in menu.items():
        print(f" {number:<5} {food[0]:<18} ₱{food[1]}")

    print("================================")


def show_cart():
    if not cart:
        print("\nYour cart is empty!")
        return

    total = 0

    print("\n--- YOUR CART ---")

    for name, price, quantity in cart:
        subtotal = price * quantity
        total += subtotal

        print(f"{name} x {quantity} = ₱{subtotal}")

    print("------------------------------")
    print(f"Total: ₱{total}")


def add_to_cart():
    show_menu()

    try:
        number = int(input("\nEnter food number: "))

        if number not in menu:
            print("Invalid food number!")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Invalid quantity!")
            return

        name, price = menu[number]

        print("\n--- CONFIRM ORDER ---")
        print(f"Item: {name}")
        print(f"Price: ₱{price}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: ₱{price * quantity}")

        confirm = input("\nIs this correct? (yes/no): ")

        if confirm.lower() == "yes":

            # If the item is already in the cart, add to its quantity
            for index, item in enumerate(cart):
                if item[0] == name:
                    cart[index] = (name, price, item[2] + quantity)
                    print("Cart quantity updated!")
                    return

            cart.append((name, price, quantity))
            print("Added to cart!")

        else:
            print("Order cancelled.")

    except ValueError:
        print("Invalid input!")


def edit_cart():
    if not cart:
        print("\nYour cart is empty!")
        return

    print("\n--- EDIT CART ---")

    for index, item in enumerate(cart, start=1):
        print(f"{index}. {item[0]} x {item[2]}")

    try:
        item_number = int(input("\nEnter item number: "))

        if not 1 <= item_number <= len(cart):
            print("Invalid item number!")
            return

        index = item_number - 1

        print("\n1. Change Quantity")
        print("2. Remove Item")

        edit_choice = input("Choose an option: ")

        if edit_choice == "1":
            quantity = int(input("Enter new quantity: "))

            if quantity > 0:
                name, price, _ = cart[index]
                cart[index] = (name, price, quantity)
                print("Quantity updated!")
            else:
                print("Invalid quantity!")

        elif edit_choice == "2":
            removed = cart.pop(index)
            print(f"{removed[0]} has been removed from your cart.")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input!")


def place_order():
    if not cart:
        print("\nYour cart is empty!")
        return

    total = sum(price * quantity for _, price, quantity in cart)

    print("\n========== RECEIPT ==========")

    for name, price, quantity in cart:
        subtotal = price * quantity

        print(f"{name}")
        print(f"Quantity: {quantity}")
        print(f"Price: ₱{price}")
        print(f"Subtotal: ₱{subtotal}")
        print("------------------------------")

    print(f"TOTAL: ₱{total}")
    print("===== ORDER PLACED! =====")

    # Save the completed order for staff to view
    orders.append({
        "items": cart.copy(),
        "total": total
    })

    cart.clear()


def view_orders():
    if not orders:
        print("\nNo orders have been placed yet.")
        return

    print("\n--- ALL ORDERS ---")

    for order_number, order in enumerate(orders, start=1):
        print(f"\nOrder #{order_number}")
        print("------------------------------")

        for name, price, quantity in order["items"]:
            subtotal = price * quantity
            print(f"{name} x {quantity} = ₱{subtotal}")

        print(f"TOTAL: ₱{order['total']}")
        print("------------------------------")


def staff_menu():
    while True:
        print("\n--- STAFF MENU ---")
        print("1. View Menu")
        print("2. Add Food")
        print("3. Remove Food")
        print("4. View Orders")
        print("5. Switch User")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            show_menu()

            try:
                number = int(input("\nEnter new food number: "))
                name = input("Enter food name: ")
                price = int(input("Enter food price: "))

                if price <= 0:
                    print("Price must be greater than zero!")
                    continue

                if number in menu:
                    print(f"\n⚠️ Item #{number} already exists: {menu[number][0]}")
                    confirm = input("Do you want to overwrite it? (yes/no): ")

                    if confirm.lower() != "yes":
                        print("Food addition cancelled.")
                        continue

                menu[number] = (name, price)
                print("Food added successfully!")

            except ValueError:
                print("Invalid input!")

        elif choice == "3":
            show_menu()

            try:
                number = int(input("\nEnter food number to remove: "))

                if number in menu:
                    removed = menu.pop(number)
                    print(f"{removed[0]} has been removed.")
                else:
                    print("Invalid food number!")

            except ValueError:
                print("Invalid input!")

        elif choice == "4":
            view_orders()

        elif choice == "5":
            print("Switching user...")
            return

        else:
            print("Invalid choice!")


def student_menu():
    while True:
        print("\n--- FOOD ORDERING SYSTEM ---")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Edit Cart")
        print("5. Place Order")
        print("6. Switch User")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            edit_cart()

        elif choice == "5":
            place_order()

        elif choice == "6":
            print("Switching user...")
            return

        else:
            print("Invalid choice!")


# MAIN LOOP
while True:
    print("\n--- LOG IN ---")
    print("1. Staff")
    print("2. Student")

    user = input("Enter user: ")

    if user == "1":
        password = input("Password: ")

        if password == "111":
            print("Hello, Staff")
            staff_menu()
        else:
            print("Incorrect password!")

    elif user == "2":
        print("Hello, Student")
        student_menu()

    else:
        print("Invalid user. Please try again!")