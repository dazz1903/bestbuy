"""Products available in the Best Buy store."""


class Product:
    """A product with a price, stock quantity, and availability status."""

    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must not be empty.")
        if price < 0:
            raise ValueError("Price must not be negative.")
        self._validate_quantity(quantity)

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    @staticmethod
    def _validate_quantity(quantity):
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self._validate_quantity(quantity)
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price:g}, Quantity: {self.quantity}")

    def buy(self, quantity):
        self._validate_quantity(quantity)
        if quantity == 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if not self.is_active():
            raise ValueError("Product is inactive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
