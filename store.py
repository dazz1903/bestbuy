"""Store inventory and orders."""

import products


class Store:
    """A collection of products that customers can purchase."""

    def __init__(self, product_list):
        self.products = list(product_list)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        # Check the whole order before changing any stock. Combine repeated
        # products so their total requested quantity is checked together.
        quantities = {}
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product is not available in this store.")
            if type(quantity) is not int or quantity <= 0:
                raise ValueError("Purchase quantity must be a positive integer.")
            if not product.is_active():
                raise ValueError("Product is inactive.")
            quantities[product] = quantities.get(product, 0) + quantity

        for product, quantity in quantities.items():
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough stock available for {product.name}.")

        total_price = 0.0
        for product, quantity in quantities.items():
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()
