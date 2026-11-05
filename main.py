"""Command-line interface for the Best Buy store."""

import products
import store


def list_products(product_list):
    for number, product in enumerate(product_list, start=1):
        print(f"{number}. ", end="")
        product.show()
    if not product_list:
        print("No active products available.")


def make_order(best_buy):
    available_products = best_buy.get_all_products()
    list_products(available_products)
    if not available_products:
        return

    shopping_list = []
    print("Enter an empty product number to finish your order.")
    while True:
        selection = input("Product number: ").strip()
        if not selection:
            break
        try:
            product_number = int(selection)
            if not 1 <= product_number <= len(available_products):
                print("Please choose a product number from the list.")
                continue
            quantity = int(input("Quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Please enter whole numbers for product and quantity.")
            continue

        product = available_products[product_number - 1]
        already_ordered = sum(
            amount for item, amount in shopping_list if item is product
        )
        if already_ordered + quantity > product.get_quantity():
            print("Not enough stock available, including items already added.")
            continue
        shopping_list.append((product, quantity))
        print("Product added to order.")

    if not shopping_list:
        print("No order placed.")
        return
    try:
        total = best_buy.order(shopping_list)
    except ValueError as error:
        print(f"Order could not be completed: {error}")
    else:
        print(f"Order completed! Total payment: ${total:.2f}")


def start(best_buy):
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        try:
            choice = input("Choose an option: ").strip()
            if choice == "1":
                list_products(best_buy.get_all_products())
            elif choice == "2":
                print(f"Total of {best_buy.get_total_quantity()} items in store.")
            elif choice == "3":
                make_order(best_buy)
            elif choice == "4":
                print("Goodbye!")
                return
            else:
                print("Please choose an option from 1 to 4.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return


def main():
    # Set up initial stock of inventory.
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
